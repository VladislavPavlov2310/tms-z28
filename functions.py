from datetime import timedelta
from time import sleep


def countdown(dttime):
    time_delta = timedelta(seconds=1)
    while (dttime.hour or dttime.minute or dttime.second) != 0:
        yield dttime
        sleep(1)
        dttime -= time_delta


def convert(hours, minutes, seconds):
    minutes += int((seconds - (seconds % 60)) / 60)
    seconds = seconds % 60
    hours += int((minutes - (minutes % 60)) / 60)
    minutes = minutes % 60
    hours = hours % 24
    return hours, minutes, seconds
