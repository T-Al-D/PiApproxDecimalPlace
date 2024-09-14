import math


def truncate_num(pi, chosen_decimal) -> float:
    """
    :param pi: 3.1415926535897932
    :param chosen_decimal: slice off the number up to this decimal place
    :return: float number that has been sliced
    """
    multiplier = 10 ** chosen_decimal
    float_value = int((pi * multiplier)) / multiplier
    return float_value


def compare_decimal_places(possible_pi, delta) -> bool:
    """
    compares wether the difference between PI_CONST and possible_pi is smaller than delta,
    then you reached your golad and calculated up to the needed decimal number
    :param possible_pi: approximatley calculated pi with lower_bound
    :param delta: float num below 0, difference between PI_CONST and cut_off chosen_decimal_place
    :return: boolean value
    """
    value = False
    epsilon = 3.1415926535897932 - possible_pi
    # decimal_places match if epsilon < delta!
    if epsilon < delta:
        value = True

    return value


def format_int_with_dot(num: int) -> str:
    return "{:,d}".format(num).replace(",", ".")


def calc_possible_pi(steps: int) -> float:
    """
    clac pi with approximate method, add up all rectangles under quader_cicle
    :param steps: amount of rectangles under the quader rectangle
    :return: calculated (possible) pi with steps
    """
    # it does not matter what radius is chosen, does not influence end result
    radius = 100
    # partial result used for end result
    quader_circle_surface = 0

    rectangle_width = radius / steps
    radius_square = radius ** 2

    # calc all rectangle under quader circle, calc height with pythagorean theorem
    # start range at 1 not 0
    for counter in range(1, steps, 1):
        current_rectangle_surface = 0
        current_triangle_width = counter * rectangle_width

        # adding a rectangle only makes sense, if width smaller than radius
        if current_triangle_width < radius:
            # the radius is the triangle_diagonal (hypotenuse)
            height_square = radius_square - (current_triangle_width ** 2)
            current_rectangle_height = math.sqrt(height_square)
            current_rectangle_surface = current_rectangle_height * rectangle_width

        # add all the rectangles together
        quader_circle_surface += current_rectangle_surface

    calculated_pi = (quader_circle_surface * 4) / radius_square
    return calculated_pi


def calc_necessary_steps_to_decimal_place(chosen_decimal: int) -> str:
    """
    epsilon is the chosen_decimal difference that is allowed
    cut_off is the middle number which gets cut off

    example delta = 3,1415 - 3,1   = 0.0415 -> 1st chosen_decimal
    example delta = 3,1415 - 3,14  = 0.0015 -> 2nd chosen_decimal
    example delta = 3,1415 - 3,141 = 0.0005 -> 3rd chosen_decimal

    :param chosen_decimal: the decimal place to where PI should be approximate to
    :return: result string for output
    """
    cut_off = truncate_num(3.1415926535897932, chosen_decimal)
    delta = 3.1415926535897932 - cut_off

    # important for phase one: iterate increase / decrease
    leap = 10 ** chosen_decimal
    previous_lower_bound = leap

    # bounds for the pi approximation
    upper_bound = None
    lower_bound = leap

    # important for phase two: smaller iterative increase / decrease (approximation)
    approximation = chosen_decimal - 1

    total_steps = 0
    result_str = ""

    while True:
        # calculate possible_pi with the amount of the lower_bound
        possible_pi = calc_possible_pi(lower_bound)
        decimalplace_correct = compare_decimal_places(possible_pi, delta)

        # 1st phase: decimal_places don´t match and upper_bound unknown -> increase lower_bound
        if upper_bound is None:
            if decimalplace_correct is False:
                previous_lower_bound = lower_bound
                lower_bound += leap
            else:
                # decimal_places match but upper_bound not set -> set upperbound, reset lower_bound one step back
                upper_bound = lower_bound
                lower_bound = previous_lower_bound

        # 2nd phase
        else:
            current_difference = upper_bound - lower_bound
            approximation_leap = 10 ** approximation

            # make numbers appear more aesthetics
            lower_bound_str = format_int_with_dot(lower_bound)
            upper_bound_str = format_int_with_dot(upper_bound)

            # update result string
            result_str += f"current low: {lower_bound_str}, current high: {upper_bound_str}, current approx.: 10^" \
                          f"{approximation}, possible pi: {possible_pi}, total steps: {total_steps}, \n"

            # "slowly" approach the upper_bound
            if decimalplace_correct is False:
                previous_lower_bound = lower_bound
                lower_bound += approximation_leap

            # overstepped upper_bound, reset a bit and approach again with smaller steps
            else:
                # with a difference of 1 or less, the bound is constricted enough
                if current_difference <= 1:
                    result_str += "MAX precision reached! \n"
                    break
                else:
                    upper_bound = lower_bound
                    lower_bound = previous_lower_bound
                    approximation -= 1

                if lower_bound == upper_bound or lower_bound + 1 == upper_bound or approximation < 0:
                    # make numbers appear more aesthetics
                    lower_bound_str = format_int_with_dot(lower_bound)
                    upper_bound_str = format_int_with_dot(upper_bound)

                    result_str += f"current low: {lower_bound_str}, current high: {upper_bound_str}, current approx.: "\
                                  f"10^{approximation}, possible pi: {possible_pi}, total steps: {total_steps}, \n"
                    result_str += "MAX precision reached!"
                    break

        total_steps += 1

    return result_str
