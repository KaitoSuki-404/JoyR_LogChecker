class Violation:

    def __init__(self, string:str):
        self.str = string

    def checkMcdError(self):
        if 'CRASHED in McdProcedural_Arnold' in self.str:
            #Something going wrong with Miarmy.
            #Check the scene to locate error.
            return 1001

    def checkError(self):
        if self.checkMcdError() != 0:
            return self.checkMcdError()
