def main():
    print(addition(2, 3))


def addition(a, b):
    return a + b


def soustraction(a, b):
    return a - b


def test_addition():
    resultat = addition(2, 3)
    assert resultat == 5


def test_soustraction():
    resultat = soustraction(42, 3)
    assert resultat == 39


def test_soustraction_2():
    resultat = soustraction(42, 4)
    assert resultat == 38


if __name__ == '__main__':
    main()
