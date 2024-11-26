class redshiftLog:

    def __init__(self, string:str):
        self.msg = string

    def checkSettingError(self):
        errorMessage = self.msg
        if 'STDOUT: [PRE] same name' in errorMessage and 'is exist.' in errorMessage:
            #AOV settings error.
            #There're multiple same name AOVs in render setting.
            return 301

    def checkLicenseError(self):
        errorMessage = self.msg
        if '[Redshift] Maxon licensing error: License not activated' in errorMessage:
            #License error.
            #License image needs to be reset.
            return 302

    def checkCameraError(self):
        errorMessage = self.msg
        if 'No renderable cameras found.' in errorMessage:
            #No camera has been set inside scene.
            #Needs to ensure that this is not due to I/O.
            return 303

    def checkLayerError(self):
        errorMessage = self.msg
        if '[Redshift] Unable to swtich to render layer:' in errorMessage:
            #Layer override error.
            #Maybe something goes on with layer name.
            return 304

    def checkError(self):
        if self.checkSettingError() != 0:
            return self.checkSettingError()
        elif self.checkLicenseError() != 0:
            return self.checkLicenseError()
        elif self.checkCameraError() != 0:
            return self.checkCameraError()
        elif self.checkLayerError() != 0:
            return self.checkLayerError()
