import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


lo = Loggable()
lo.log('123')


class LoggableList(list, Loggable):
    def append(self, elem):
        self.log(elem)
        super().append(elem)


l = LoggableList()
l.append(1)
