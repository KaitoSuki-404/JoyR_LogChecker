import sys
sys.path.append('../lib')

#Cloud-machine specialized
sys.path.append('C:/Kaito/script/logChecker/lib')

#C-like macro manifesto
ARNOLD = 0
REDSHIFT = 1

#Import text check module
from Judge import CheckText

#Insert essential parameters for analysis
filePath = input("insert log file path: ")
mode = input("renderer mode(ARNOLD;REDSHIFT): ")

#Error sheet
errors = {'101': '[Memory] Address invalid! Insertion failed',
          '201': '[XGen] File went wrong on importing.',
          #Redshift errors
          '301': '[Redshift] Multiple same name AOVs detected.',
          '302': '[Redshift] License error, needs to update license server.',
          '303': '[Redshift] No renderable camera found.',
          #Maya errors
          '401': '[Maya] Default layer name is corrupted. Needs to manually change through document.',
          #Houdini errors
          '901': '[Houdini] Segmentation error! Maybe something going on with scene.',
          #Access violation errors
          '1001': '[Violation] Miarmy exported assets error',
          #Appears to perform well
          None: 'Appears to perform well'
          }

#Main loop for line-by-line check
with open(filePath, "r", encoding='utf-8') as file:
    line = file.readline()
    while line:

        info = CheckText(line, mode)
        returnCode = info.checkLog()

        line = file.readline()

    error = errors[returnCode]
    print(error)