


from CosdLogger import CosdLogger
from LogTestClassB import LogTestClassB

class LogTestClassA:
    def __init__(self, log):
        self.logit = log

    def class_test(self, msg):
        self.logit.log("test logger from inside method inside a class with message= " + msg)

#test comment directly above TestLogger method
def TestLogger(msg):
    logutil.log(msg)

logutil = CosdLogger("..\\Logs", None)

logutil.log("test in root of script")

#test comment directly above function call
logutil.log("test with comment above root function call")
TestLogger("test logger from inside root method")

logTestA = LogTestClassA(logutil)
logTestA.class_test("test method from inside internal class")

logTestB = LogTestClassB(logutil)
logTestB.class_test("test method with logger passed to external class")