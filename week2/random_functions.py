# random functions
def print_loop_progress(index, iterations):
    progress_bar = "|"
    bar_segments = 20
    complete = index//(iterations//bar_segments)
    remain = bar_segments-complete
    for i in range(complete):
        progress_bar += "X"
    for j in range(remain):
        progress_bar += "-"
    progress_bar += "|"
    print(progress_bar, index, "/", iterations, end='\r')

    if complete+1 == bar_segments:
        progress_bar = "  "
        for i in range(bar_segments):
            progress_bar += " "
        print(progress_bar, end='\r')


def break_if_equal(index, var1, var2):
    if var1 == var2:
        print(index+1)
        return "break"
