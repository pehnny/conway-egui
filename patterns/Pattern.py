type RelativeCoordinates = list[tuple[int, int]]

class Pattern:
    def __init__(self) -> None:
        self.pattern: RelativeCoordinates = [(0, 0)]

    def get_pattern(self) -> RelativeCoordinates:
        return self.pattern

    def set_pattern(self, coordinates: RelativeCoordinates) -> None:
        self.pattern = coordinates
        return
