from pygame import time

timer_list = []


def game_timers():
    if len(timer_list) > 0:
        for timer in timer_list:
            if timer.timer_ring:
                timer_list.pop(timer_list.index(timer))
            else:
                timer.run_timer()


class Timer():
    def __init__(self, func=None):
        self.timer_ring = False
        self.start_time = time.get_ticks()
        self.current_time = 0
        self.length = 1000
        self.func = func

    def run_timer(self):
        self.current_time = time.get_ticks()

        if self.current_time - self.start_time > self.length:
            self.timer_ring = True
            if self.func is None:
                return True
            else:
                self.func()



