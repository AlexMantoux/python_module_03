from math import sqrt
import sys

class FormatError(Exception):
    pass

def remarkable_id(x1: int, x2: int) -> int:
    return (x1 * x1) - (2 * x1 * x2) + (x2 * x2)

def compute_distance(point1: tuple[int, int, int], point2: tuple[int, int, int]) -> float:

    x1, y1, z1 = point1
    x2, y2, z2 = point2

    return sqrt(remarkable_id(x2, x1) + remarkable_id(y2, y1) + remarkable_id(z2, z1))

def parse_to_tuple(string: str) -> tuple[int, int, int] | None:
    ret = string.strip()
    ret = ret.split(",")
    if len(ret) != 3:
            raise FormatError("Wrong number of digits can't be parsed to tuple[int, int, int]")
    try:
        for i in range(len(ret)):
            ret[i] = int(ret[i])
        return tuple(ret)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        raise ValueError(f"Error details - Type ValueError, Args: (\"{e}\",)")

if __name__ == "__main__":

    args = sys.argv
    p2 = (0, 0, 0)
    print("=== Game Coordinate System ===\n")
    if (len(args) != 2):
        p1 = (10, 20, 5)
        print(f"Position created: {p1}")
        print(f"Distance between {p2} and {p1}: {compute_distance(p1, p2): .2f}")
        print()
        p1 = "3,4,0"
        print(f"Parsing coordinates: \"{p1}\"")
        print(f"Parsed position: {parse_to_tuple(p1)}")
        print(f"Distance between {p2} and {p1}: {compute_distance(parse_to_tuple(p1), p2): .1f}")
        print()
        p1 = "abc,def,ghi"
        print(f"Parsing coordinates: \"{p1}\"")
        try:
            res = parse_to_tuple(p1)
        except (ValueError, FormatError) as e:
            print(f"{e}")
        print()
        p1 = (3, 4, 0)

        
        print("Unpacking demonstration:")
        print(f"Player at x={p1[0]}, y={p1[1]}, z={p1[2]}")
        x, y, z = p1
        print(f"Coordinates: X={x}, Y={y}, Z={z}")

    elif len(args) == 2:
        p1 = args[1]
        print(f"Parsing coordinates: \"{p1}\"")
        try:
            res = parse_to_tuple(p1)
            print(f"Parsed position: {res}")
            print(f"Distance between {p2} and {res}: {compute_distance(res, p2): .1f}")
        except (ValueError, FormatError) as e:
            print(f"{e}")

