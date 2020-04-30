class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """Create a MyTime object initialized to hrs, mins, secs """
        self.hours = hrs
        self.minutes = mins
        self. seconds = secs

        totalsecs = hrs * 3600 + mins * 60 + secs
        self.hours = totalsecs // 3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60


    def add_time(t1, t2):
        secs = t1.to_seconds() + t2.to_seconds()
        return MyTime(0, 0, secs)

    def to_seconds(self):
        """ Return the number of seconds represented by this instance"""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def between(self, t1, t2):

        if t1 <= self < t2:
            return "True"
        else
            return "False"
