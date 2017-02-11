from PIL import Image
import ctypes, sys, os

'''
1    #蓝色        0        0        255
2    #绿色        0        255      0
3    #天蓝色      0        255      255
4    #红色        255      0        0
5    #粉红色      255      0        255  
5    #粉红色      255      0        255   
6    #黄色        255      255      0  
7    #白色        255      255      255
0x01 ~ 0x07 是 字色 （浅）
0x09 ~ 0x0f 是 字色 （深）
0x10 ~ 0x70 是 背景色 （浅）
0x90 ~ 0xf0 是 背景色 （深）
'''

STD_OUTPUT_HANDLE = ctypes.windll.kernel32.GetStdHandle(-11)  # 控制台句柄
def printcolor(color, str):
    ctypes.windll.kernel32.SetConsoleTextAttribute(STD_OUTPUT_HANDLE, color)
    sys.stdout.write(str)
    sys.stdout.flush()            # 处理缓冲区

ColorUnitVector = [[255,255,255],[255,255,0],[255,0,255],[255,0,0],[0,255,255],[0,255,0],[0,0,255]]
sqy = [442,360,360,255,360,255,255]           # (ColorUnitVector**2).sum(axis=1)**0.5
ascii_char = " .vijtkd$#@vvviiijjjtttkkkddd$$$###@@@@@@@@#####$$$$$dddddkkkkktttttjjjjjiiiiivvvvv.....     "
unit = 256 / len(ascii_char)        # 每个字符对应的灰度范围

def rgb2char(x):
    gray = 0.213*x[0] + 0.715*x[1] + 0.072*x[2]    # 灰度
    char_index = int(gray/unit)                     # 字符对应的索引
    max_cos = 0
    best_color = 0
    for i in range(7):
        y = ColorUnitVector[i]
        numerator = x[0]*y[0] + x[1]*y[1] + x[2]*y[2]
        denominator = ((x[0]**2 + x[1]**2 + x[2]**2)**0.5) * sqy[i]
        v_cos = numerator / (denominator + 0.1)
        # if v_cos > 0.9:
        #     return char_index, 7 - i
        if v_cos > max_cos:
            max_cos = v_cos
            best_color = i
    return char_index, 7 - best_color

def showImage(filename = 'test.jpg', MaxWith = 400, k = 1.7):
    im = Image.open(filename)
    if(im.size[0] > MaxWith):
        WIDTH, HEIGHT = MaxWith, int((MaxWith * im.size[1] / im.size[0]) / k)
    else:
        WIDTH,HEIGHT = im.size[0], int(im.size[1] / k)
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
    for h in range(HEIGHT):  
        for w in range(WIDTH):
            pixel = im.getpixel((w, h))
            i,c = rgb2char(pixel)
            if(i > 10): c = c + 8
            if(i > 37): c = c << 4
            printcolor(c, ascii_char[i])
        printcolor(0x0f, '\n')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        showImage(sys.argv[1])
    elif len(sys.argv) == 3:
        showImage(sys.argv[1],int(sys.argv[2]))
    elif len(sys.argv) == 4:
        showImage(sys.argv[1],int(sys.argv[2]),float(sys.argv[3]))
    else:
        showImage()
