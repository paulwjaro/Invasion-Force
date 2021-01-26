from pygame import time


class Timer:
    def __init__(self, _length=1000, _func=None):
        self.timer_ring = False
        self.start_time = time.get_ticks()
        self.current_time = 0
        self.length = _length
        self.func = _func

    def run_timer(self):
        self.current_time = time.get_ticks()

        if self.current_time - self.start_time > self.length:
            self.timer_ring = True
            if self.func is None:
                return True
            else:
                self.func()


def create_timer(self, _func=None):
    new_timer = Timer(_func=_func)
    self.timers.append(new_timer)


def run_timers(self):
    if len(self.timers) > 0:
        for t in self.timers:
            if not t.timer_ring:
                t.run_timer()
            else:
                self.timers.pop(self.timers.index(t))
