def main() -> None:
    print(addition(2, 3))


def addition(a: int, b: int) -> int:
    return a + b


def soustraction(a: int, b: int) -> int:
    return a - b


def test_addition() -> None:
    resultat = addition(2, 3)
    assert resultat == 5


def test_soustraction() -> None:
    resultat = soustraction(42, 3)
    assert resultat == 39


def test_soustraction_2() -> None:
    resultat = soustraction(42, 4)
    assert resultat == 38


if __name__ == "__main__":
    main()
