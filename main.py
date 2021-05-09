
def par_k(a: float, b: float) -> float:
    return 2 * a + 2 * b


def par_t(a: float, b: float, ma: float, mb: float) -> float:
    terulet = a * mb or b * mb
    if a * mb != b * mb:
        print('Az a * ma egyenlő a b * mb-vel!')
    else:
        return terulet


def Main() -> None:
    print('Paralelogramma K és T:')
    a: float = float(input("a= "))
    b: float = float(input("b= "))
    ma: float = float(input("ma= "))
    mb: float = float(input("mb= "))
    if a * ma <= 0 or b * mb <= 0:
        print('Nincs ilyen paralelogramma')
    else:
        print(f'Paralelogramma kerülete: {par_k(a, b,)}')
        print(f'Paralelogramma területe: {par_t(a, b ,ma ,mb)}')


if __name__ == "__main__":
    Main()
