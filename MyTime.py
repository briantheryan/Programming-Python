class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """Create a MyTime object initialized to hrs, mins, secs """
        self.hours = hrs
        self.minutes = mins
        self.seconds = secs

        totalsecs = hrs * 3600 + mins * 60 + secs
        self.hours = totalsecs // 3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __gt__(self, t2):
        return self.after(t2)

    def add_time(t1, t2):
        secs = t1.to_seconds() + t2.to_seconds()
        return MyTime(0, 0, secs)

    def to_seconds(self):
        """ Return the number of seconds represented by this instance"""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def between(self, t1, t2):
        """ Returns TRUE if time lies between t1 and t2"""
        return t1.to_seconds() <= self.to_seconds() < t2.to_seconds()

    def after(self, time2):
        """Returns TRUE if self is greater than time2"""
        return self.to_seconds() > time2.to_seconds()

    def increment(self, secs):
        secs = self.to_seconds() + secs.to_seconds()
        self.hours = secs // 3600
        leftoversecs = secs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60
        return self.hours, self.minutes, self.seconds