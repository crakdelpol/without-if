if __name__ == "__main__":

    arrayOfIntegers = [1, 4, 5, 9, 0, -1, 5]

    result = 0
    for integer in arrayOfIntegers:
        result += integer % 2

    print(result)
