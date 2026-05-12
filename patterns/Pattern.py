from dataclasses import dataclass

type RelativeCoordinates = list[tuple[int, int]]

@dataclass
class Pattern:
    name: str
    coordinates: RelativeCoordinates
    
    def size(self) -> int:
        x_min, y_min = 0, 0
        x_max, y_max = 1, 1

        for x, y in self.coordinates:
            x_min = min(x, x_min)
            y_min = min(y, y_min)
            x_max = max(x + 1, x_max)
            y_max = max(y + 1, y_max)

        return max(x_max - x_min, y_max - y_min)
