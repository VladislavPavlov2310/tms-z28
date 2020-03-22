class MyTime:
    def __init__(self, *args):
        if len(args) == 1 and type(args[0]) == str:
            self.tmp_list = list(args)
            self.tmp_list = self.tmp_list[0].split()
            self.hours = int(self.tmp_list[0])
            self.minutes = int(self.tmp_list[1])
            self.seconds = int(self.tmp_list[2])
        elif len(args) == 3:
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif len(args) == 1 and type(args[0]) == MyTime:
            self.hours = args[0].hours
            self.minutes = args[0].minutes
            self.seconds = args[0].seconds
        else:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0

        if self.seconds >= 60:
            self.minutes += int((self.seconds - (self.seconds % 60)) / 60)
            self.seconds = self.seconds % 60
        if self.minutes >= 60:
            self.hours += int((self.minutes - (self.minutes % 60)) / 60)
            self.minutes = self.minutes % 60
        if self.hours >= 24:
            self.hours = self.hours % 24

    def __str__(self):
        return f'Time: {self.hours}:{self.minutes}:{self.seconds}'

    def __eq__(self, other):
        return (
                self.hours == other.hours and
                self.minutes == other.minutes and
                self.seconds == other.seconds
        )

    def __ne__(self, other):
        return (
                self.hours != other.hours and
                self.minutes != other.minutes and
                self.seconds != other.seconds
        )

    def __lt__(self, other):
        if self.hours == other.hours:
            if self.minutes == other.minutes:
                if self.seconds < other.seconds:
                    return True
                else:
                    return False
            elif self.minutes < other.minutes:
                return True
            else:
                return False
        elif self.hours < other.hours:
            return True
        else:
            return False

    def __gt__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        if self.hours == other.hours:
            if self.minutes == other.minutes:
                if self.seconds <= other.seconds:
                    return True
                else:
                    return False
            elif self.minutes < other.minutes:
                return True
            else:
                return False
        elif self.hours < other.hours:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.__le__(other) is True and self.seconds == other.seconds:
            return True
        else:
            return False

    def __add__(self, other):
        return MyTime(
            self.hours + other.hours,
            self.minutes + other.minutes,
            self.seconds + other.seconds
        )

    def __sub__(self, other):
        return MyTime(
            self.hours - other.hours,
            self.minutes - other.minutes,
            self.seconds - other.seconds
        )

    def __mul__(self, other: int):
        return MyTime(
            self.hours * other,
            self.minutes * other,
            self.seconds * other
        )



