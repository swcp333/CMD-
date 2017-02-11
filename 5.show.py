import ctypes, sys
import os, pickle, time

STD_OUTPUT_HANDLE = ctypes.windll.kernel32.GetStdHandle(-11)
class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

def printcolor(x, y, str, color):
    print_xy = COORD()
    print_xy.X = x
    print_xy.Y = y
    ctypes.windll.kernel32.SetConsoleCursorPosition(STD_OUTPUT_HANDLE, print_xy)
    ctypes.windll.kernel32.SetConsoleTextAttribute(STD_OUTPUT_HANDLE, color)
    sys.stdout.write(str)
    sys.stdout.flush()

def show_cmd(filename = r'cmddiff\0.pickle'):
    with open(filename,'rb') as f:
        diff = pickle.load(f)
    for pixel in diff:
        printcolor(*pixel)
    l = len(diff) / 10000
    if(l < 0.08):
        time.sleep(0.08 - l)

if __name__ == '__main__':
    for i in range(len(os.listdir('cmddiff\\'))):
        cmddiffFile = r'cmddiff\%d.pickle' % i
        show_cmd(cmddiffFile)
    