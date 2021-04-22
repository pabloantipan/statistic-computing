def recursiveFibo(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return recursiveFibo(n - 1) + recursiveFibo(n - 2)


def dinamicFibo(n: int, memo: dict = {}) -> int:
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError:
        result = dinamicFibo(n - 1, memo) + dinamicFibo(n - 2, memo)
        memo[n] = result

        return result


if __name__ == "__main__":
    n = int(input("Give me a number, please: "))
    result = dinamicFibo(n)
    print(result)