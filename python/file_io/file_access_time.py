import os, stat, shutil

idx = 1;
old_atime = 0;

while True:
    stats = os.stat('image.bmp')

    if stats.st_atime != old_atime:
        if idx == 1:
            shutil.copyfile('image2.bmp', 'image.bmp')
            print("copying image2.bmp")
            idx = 2;
        else :
            shutil.copyfile('image1.bmp', 'image.bmp')
            print("copying image1.bmp")
            idx = 1

        stats = os.stat('image.bmp')
        old_atime = stats.st_atime

