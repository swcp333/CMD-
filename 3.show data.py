import ctypes, sys
import os

STD_OUTPUT_HANDLE = ctypes.windll.kernel32.GetStdHandle(-11)
class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]
def printcolor(color, str, x, y):
    print_xy = COORD()
    print_xy.X = x
    print_xy.Y = y
    ctypes.windll.kernel32.SetConsoleCursorPosition(STD_OUTPUT_HANDLE, print_xy)
    ctypes.windll.kernel32.SetConsoleTextAttribute(STD_OUTPUT_HANDLE, color)
    sys.stdout.write(str)
    sys.stdout.flush()

def show_cmd(filename = r'cmdout\0.cmdout'):
    with open(filename, 'r') as f:
        row = f.readlines()
    for y,line in enumerate(row):
        line = line.split('\t')[:-1]  # 去掉最后一个换行符
        for x,pixel in enumerate(line):
            ch = pixel[0]
            co = int(pixel[1:])
            printcolor(co, ch, x, y)
        printcolor(0x0f, '\n', x, y)

if __name__ == '__main__':
    show_cmd()
    for i in range(len(os.listdir('images\\'))):
        cmdoutFile = r'cmdout\%d.cmdout' % i
        show_cmd(cmdoutFile)