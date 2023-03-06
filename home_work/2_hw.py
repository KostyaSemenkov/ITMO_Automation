def task_1(a: int = 1, b: float = 1.1, c: str = 'lemur', d: list = [1, 2, 3], e: bool = True) -> object:
    return print(type(a), type(b), type(c), type(d), type(e))
task_1()


def task_2(a: list = [1, 2, 3, 5, 8, 13, 21]) -> str:
    return print(*a[:3]) # это распакованный срез списка
task_2()


def task_3(number: int) -> int :
    return print(number ** 2)
task_3(3)
