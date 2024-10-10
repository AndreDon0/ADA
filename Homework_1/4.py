class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __add__(self, other):
        other_minute = other % 60
        other_hour = other // 60
        self.hour = (self.hour + other_hour + (self.minute + other_minute) // 60) % 24
        self.minute = (self.minute + other_minute) % 60
        return self

    def __str__(self):
        return f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}"


H = int(input())
M = int(input())
T = int(input())

clock = Clock(H, M)
clock += T
print(clock)
