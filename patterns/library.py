from patterns.Pattern import Pattern

LIBRARY = {
    "default" : Pattern(
        "default", 
        [(0, 0)]
    ),
    "glider" : Pattern(
        "glider",
        [
            (1, 0),
            (2, 1),
            (0, 2),
            (1, 2),
            (2, 2)    
        ]
    ),
}
