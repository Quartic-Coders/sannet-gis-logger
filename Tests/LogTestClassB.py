

class LogTestClassB:
    def __init__(self, log):
        self.logit = log

    def class_test(self, msg):
        self.logit.log("test logger from inside method inside a class with message: " + msg)


if __name__=="__main__":
    __main__