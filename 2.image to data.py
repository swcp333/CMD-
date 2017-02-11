from PIL import Image
import os

ColorUnitVector = [[255,255,255],[255,255,0],[255,0,255],[255,0,0],[0,255,255],[0,255,0],[0,0,255]]
sqy = [442,360,360,255,360,255,255]
ascii_char = " .vijtkd$#@vvviiijjjtttkkkddd$$$###@@@@@@@@#####$$$$$dddddkkkkktttttjjjjjiiiiivvvvv.....     "
unit = 256 / len(ascii_char)
def rgb2char(x):
    gray = 0.213*x[0] + 0.715*x[1] + 0.072*x[2]
    char_index = int(gray/unit)
    max_cos = 0
    best_color = 0
    for i in range(7):
        y = ColorUnitVector[i]
        numerator = x[0]*y[0] + x[1]*y[1] + x[2]*y[2]
        denominator = ((x[0]**2 + x[1]**2 + x[2]**2)**0.5) * sqy[i]
        v_cos = numerator / (denominator + 0.1)
        # if v_cos > 0.95:
        #     return char_index, 7 - i
        if v_cos > max_cos:
            max_cos = v_cos
            best_color = i
    return char_index, 7 - best_color

def image2cmdout(im_in, cmd_out, MaxWith = 300):
    im = Image.open(im_in)
    if(im.size[0] > MaxWith):
        WIDTH, HEIGHT = MaxWith, int((MaxWith * im.size[1] / im.size[0]) / 1.9)
    else:
        WIDTH,HEIGHT = im.size[0], int(im.size[1] / 1.9)
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
    with open(cmd_out, 'w') as f:
        for h in range(HEIGHT):  
            for w in range(WIDTH):
                pixel = im.getpixel((w, h))
                i,c = rgb2char(pixel)
                if(i > 10):
                    c = c + 8
                if(i > 37):
                    c = c << 4
                f.write('%s%d\t' % (ascii_char[i],c))
            f.write('\n')

if __name__ == '__main__':
    for i in range(len(os.listdir('images\\'))):
        imageFile = r'images\%d.jpg' % i
        cmdoutFile = r'cmdout\%d.cmdout' % i
        image2cmdout(imageFile, cmdoutFile, 200)
        print('%d 转换完成' % i)
