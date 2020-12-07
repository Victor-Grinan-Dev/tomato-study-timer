import time as tm
from datetime import timedelta
from study_timer import tomato_timer_ui as ttu
from study_timer import timer_study as ts



def countdown(time):
    ts.down_counter = True

    counter_top = timedelta(seconds=time)  # convert integer into time
    mins, secs = divmod(time, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    ttu.counter_label['text'] = counter_top
    counter_top -= 1

    if counter_top == 0:
        ttu.counter_label['text'] = "00:00"
        ts.down_counter = False
        ttu.popout()
        return 0

    def study_countdown(time):

        study_time = time  # * 60 converting mins to secs

        mins, secs = divmod(study_time, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        ttu.counter_label['text'] = timeformat

        study_time -= 1

        if study_time == 0:
            ttu.counter_label['text'] = "00:00"
            ttu.popout()
            return 0

        ttu.window.after(1000, study_countdown)

    ttu.window.after(1000, countdown)