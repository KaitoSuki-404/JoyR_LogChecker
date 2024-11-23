class globalLog:

    def __init__(self, string:str):
        self.msg = string

    def checkLayerError(self):
        errorMessage = self.msg
        if 'Unable to modify overrides to the default layer' in errorMessage:
            #Case1:the scene has set material override inside render settings.
            #Case2:the masterLayer's name of the scene has changed.Which can be managed
            #through the document below.
            #https://note.youdao.com/s/RCX4YisR
            return 401
        return 0

    def checkAssetsError(self):
        errorMessage = self.msg
        if 'Error: XGen:  Failed to open file:' in errorMessage:
            #XGen's file went wrong on importing.
            return 201
        return 0

    def checkHoudiniCrash(self):
        errorMessage = self.msg
        if 'Fatal error: Segmentation fault' in errorMessage:
            #Houdini application crashed.
            return 901

    def checkError(self):
        if self.checkAssetsError() != 0:
            return self.checkAssetsError()
        elif self.checkLayerError() != 0:
            return self.checkLayerError()
        #Others
        return 0