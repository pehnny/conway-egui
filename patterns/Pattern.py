from config import RelativeCoordinates
from dataclasses import dataclass

@dataclass
class Pattern:
    name: str
    coordinates: RelativeCoordinates
    size: int = 0
    
    def get_size(self) -> int:
        if self.size != 0 :
            return self.size
        
        x_min, y_min = 0, 0
        x_max, y_max = 1, 1

        for x, y in self.coordinates:
            x_min = min(x, x_min)
            y_min = min(y, y_min)
            x_max = max(x + 1, x_max)
            y_max = max(y + 1, y_max)

        self.size = max(x_max - x_min, y_max - y_min)

        return self.size
