# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 01:43:14 2018

@author: ponju
"""

from PIL import Image
import argparse

# 参数配置
parser = argparse.ArgumentParser(description='Image to ASCII Art')
parser.add_argument('-o', '--output')  # 输出文件
parser.add_argument('--width', type=int, default = 120)  
parser.add_argument('--height', type=int, default = 60)  

args = parser.parse_args()

WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

char_string = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def rgb2char(r, g, b):
    
    length = len(char_string)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length 
    return char_string[int(gray / unit)]


if __name__ == '__main__':

    im = Image.open('test.jpg')
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += rgb2char(*im.getpixel((j,i)))
        txt += '\n'

    print(txt)

    #字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)
   
    print("恭喜，转换成功！")
    input()
