class arnoldLog:

    def __init__(self, string:str):
        self.msg = string

    def checkMemError(self):
        errorMessage = self.msg
        if 'signal caught: error C0000005 -- access violation' in errorMessage:
            #Memory write error.
            #May occurs in many circumstances.
            return 101
        return 0

    def checkNodeError(self):
        errorMessage = self.msg
        if '[Process] - Node ' in errorMessage and ' is not exist.' in errorMessage:
            #Houdini error.
            #Normally output node doesn't exist in hip.
            #Tell client to re-upload the hip file specifies.
            return 902
        return 0

    def checkError(self):
        if self.checkMemError() != 0:
            return self.checkMemError()
        elif self.checkNodeError() != 0:
            return self.checkNodeError()
        #Others
        return 0
