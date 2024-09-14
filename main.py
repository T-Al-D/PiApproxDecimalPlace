import signal
import time

from gooey import Gooey, GooeyParser

from Calc import calc_necessary_steps_to_decimal_place
from CheckInput import check_input


@Gooey(language="english",
       default_size=(675, 500),
       shutdown_signal=signal.CTRL_C_EVENT)
def gui() -> None:
    """
    starts a GUI Interface for the User, Methods can be called here
    :return: None
    """
    # add everything you need on your GUI to the parser
    parser = GooeyParser(description="Calculate steps needed to calculate PI chosen decimal place (1-7)")

    # define a group for ascetic appearance
    group1 = parser.add_argument_group("Calculate the steps to a chosen decimal place",
                                       gooey_options={"show_border": True})
    # add all the widgets you need for the input
    group1.add_argument("userinput", type=check_input, help="Please input number for calculation...")

    # output and show the GUI
    args = parser.parse_args()
    # access the input in the field with the "identifier"
    user_input = args.userinput

    # normal method execution
    start = time.time()
    result_string = calc_necessary_steps_to_decimal_place(user_input)
    end = time.time()

    # print on display like on console
    print(result_string)
    print(f"Time needed:  {round(end - start, 3)} seconds. \n")


if __name__ == '__main__':
    gui()
