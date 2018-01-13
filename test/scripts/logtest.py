


from sannetlogger import SannetLogger

def log_info(msg):
    log.log(msg)
    print msg


def log_debug(msg):
    log.log("Error occurred:"+msg)
    print msg
    global send_debug_email
    send_debug_email = True
    
#test comment directly above TestLogger method
def TestLogger(msg):
    log.log(msg)

log = SannetLogger("..\\Logs")

log.log("test in root of script")

#test comment directly above function call
log.log("test with comment above root function call0")
TestLogger("test logger from inside root method0")
log_debug("test logger from inside root method0")
log_info("test logger from inside root method0")

