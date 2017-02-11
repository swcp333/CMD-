import os

def getImage(crop_time = 0, crop_time_max = 20, frame = 12, filename = 'test.flv'):
    i = 0
    time = 1 / frame
    while crop_time <= crop_time_max :
        # -v quiet：静默工作，不输出版本、工作信息
        # -threads：多线程
        # -i 设定输入
        # -ss 开始时间
        # -f 设定输出格式
        os.system(r'ffmpeg -v quiet -threads 3 -i %s -ss %s -f image2 -vframes 1 images\%s.jpg' % (filename, crop_time, i))
        i += 1
        crop_time += time
        print('%.2f' % crop_time)
    print('--- 完成 ---')

if __name__ == '__main__':
    getImage()
