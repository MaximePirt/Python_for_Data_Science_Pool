import os
import time
import sys


def get_time_str(seconds):
    """ This function return time from seconds given by time.time()
        Use format HMS (00:00:00) if hours, or MS (00:00) if not
        return type is string
    """
    seconds = max(0, int(seconds))
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    if hours:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    else:
        return f"{minutes:02d}:{seconds:02d}"


def ft_tqdm(lst: range) -> None:
    """ TQDM copy function """

    start_time = time.time()  # Start timer
    lst_len = len(lst)
    if lst_len == 0:
        return

    i = 1
    for elem in lst:
        current_time = time.time()
        calcultime = current_time - start_time

        columns = os.get_terminal_size().columns
        pourcent = str(int(i / lst_len * 100))

        left_part = pourcent + "%|"
        right_parts = "| " + str(i) + "/" + str(lst_len) + " []"

        if calcultime > 0:  # Check if forecast is usable
            rate = i / calcultime
            remaining = (lst_len - i) / rate
            right_parts += get_time_str(calcultime) + "<"
            right_parts += get_time_str(remaining)
            right_parts += ", " + f"{rate:.2f}" + "it/s]"
        else:
            right_parts += get_time_str(0)
            right_parts += "<?, ?it/s]"

        term_size = columns - len(left_part) - len(right_parts)
        if (term_size < 1):
            term_size = 1

        gap = int((i / lst_len) * term_size)
        void = term_size - gap

        line = "\r"
        line += left_part
        line += "█" * gap
        line += " " * void
        line += right_parts

        sys.stdout.write(line)
        sys.stdout.flush()
        yield elem
        i += 1

    sys.stdout.write("\n")

    return
