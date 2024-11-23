from checkArnoldLog import *
from checkRedshiftLog import *
from checkLoadingLog import *

class CheckText:

    def __init__(self, string:str, mode:int):
        self.string = string
        self.mode = mode

    def checkLog(self):
        # Check global errors
        log = globalLog(self.string)
        errorCode = log.checkError()
        if errorCode == 0:
            #Check renderer's individual errors
            if self.mode == 0:
                log = arnoldLog(self.string)
                errorCode = log.checkError()
            elif self.mode == 1:
                log = redshiftLog(self.string)
                errorCode = log.checkError()
        if errorCode != 0:
            print(errorCode)
            return errorCode
