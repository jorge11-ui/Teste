# Dataclasses

# O que aprender:
# - @dataclass reduz __init__/__repr__/__eq__
# - field(default_factory=...)
# - frozen=True para imutável

from dataclasses import dataclass
import dataclasses

@dataclass
class Point():
    x: int
    y: int

point = Point(1, 2)
print(point)


