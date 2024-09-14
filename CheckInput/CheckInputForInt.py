
def check_input(possible_num: str) -> int:
    """
    return positive int (convert negative or float) or None
    :param possible_num: input from user as string
    :return: number between 1 and 7 or exception
    """
    try:
        possible_num = abs(float(possible_num))
        possible_num = int(possible_num)
        if 0 < possible_num < 8:
            print(f"The input was valid: {possible_num}! \n")
            return possible_num
        else:
            print("Only Numbers between 1 and 7 ! \n")
    except ValueError:
        print("This is not a number! \n")
