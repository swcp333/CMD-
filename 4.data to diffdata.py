import os, pickle
# import random
def cmdout2cmddiff(now):   # 从1开始，和前一个比较
    f1name = r'cmdout\%d.cmdout' % now
    f2name = r'cmdout\%d.cmdout' % (now-1)
    with open(f1name, 'r') as f:
        f1 = f.readlines()
    with open(f2name, 'r') as f:
        f2 = f.readlines()
    diff_line = []
    for y,line1 in enumerate(f1):
        line1 = line1.split('\t')[:-1]
        line2 = f2[y].split('\t')[:-1]
        for x,pixelnow in enumerate(line1):
            pixellast = line2[x]
            if(pixelnow != pixellast):
                diff_line.append((x,y,pixelnow[0],int(pixelnow[1:])))      
    # random.shuffle(diff_line)
    outname = r'cmddiff\%d.pickle' % now
    with open(outname,'wb') as f:
        pickle.dump(diff_line,f)
                    

if __name__ == '__main__':
    with open(r'cmdout\0.cmdout', 'r') as f:
        row = f.readlines()
    diff_line = []
    for y,line in enumerate(row):
        line = line.split('\t')[:-1]
        for x,pixel in enumerate(line):
            diff_line.append((x,y,pixel[0],int(pixel[1:])))
    with open(r'cmddiff\0.pickle','wb') as f:
        pickle.dump(diff_line,f)
    for i in range(1,len(os.listdir('cmdout\\'))):
        cmdout2cmddiff(i)
        print(i)