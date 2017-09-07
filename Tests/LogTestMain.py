


from CosdLogger import CosdLogger

#test comment directly above TestLogger method
def TestLogger():
    logutil.Log("test logger from inside method")

logutil = CosdLogger()

logutil.Log("test in root of script")

#test comment directly above function call
logutil.Log("test with comment above function call")