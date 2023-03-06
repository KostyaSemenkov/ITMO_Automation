a: int = 5
b: str = 'строка'
c: list = [1, 2]
def indent(s: str, width: int) -> str:
    return ' ' * (max(0, width - len(s))) + s


print(indent('123', 123))

def ae(s: str = '') -> int:
    return len(s)


def aw(x: list, y: list) -> int:
    return len(max(x, y))