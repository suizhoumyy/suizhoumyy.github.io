#!/usr/bin/env python3
# coding=utf-8
u"""将图片的宽度压缩到900px"""

from PIL import Image
import os
import sys
import getopt
from multiprocessing import Pool
from img_rotate import fix_orientation

poolLimite = 10
basewidth = 900
key = "lQ_pMeGpf_kYWVP28KV4DFy1pXnvFpwv"
opts, args = getopt.getopt(sys.argv[1:], "hi:o:r:")
input_doc_path = ""
output_doc_path = ''
filePaths = []

for op, value in opts:
    if op == "-i":
        input_doc_path = value
    elif op == "-o":
        output_doc_path = value
    elif op == "-r":
        input_doc_path = value
        output_doc_path = value
    elif op == "-h":
        print('''
        使用方法 python3 resize_image.py -i picDocPath -o outputDocPath
        -o 参数可以为空，默认覆盖原有的图片
        ''')


def absFilePath(fileName):
    u"""绝对路径"""
    return os.path.join(input_doc_path, fileName)

def resizeimage(filePath):
    u"""压缩"""
    image = Image.open(filePath)
    print('开始' + filePath + ': ', image.size)
    if image.size[0] > basewidth:
        print(filePath, "resize")
        wpercent = float(basewidth) / float(image.size[0])
        hsize = int(wpercent * float(image.size[1]))
        image = image.resize((basewidth, hsize), Image.ANTIALIAS)
        image.save(filePath, quality=100)

def main():
    global output_doc_path
    if output_doc_path == '':
        output_doc_path = input_doc_path

    for parent, dirnames, filenames in os.walk(input_doc_path):    # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for dirname in dirnames:                       # 输出文件夹信息
            outDir = os.path.join(output_doc_path, os.path.relpath(os.path.join(parent, dirname), input_doc_path))
            if not os.path.exists(outDir):
                os.mkdir(outDir)

        for filename in filenames:                        # 输出文件信息
            filePaths.append(os.path.join(parent, filename))

    pngFilePaths = filter(lambda x: os.path.splitext(x)[1] == '.png' or os.path.splitext(x)[1] == '.jpg' or os.path.splitext(x)[1] == '.jpeg', filePaths)
    print('Parent process %s.' % os.getpid())
    p = Pool(poolLimite)
    for fileName in pngFilePaths:
        p.apply_async(resizeimage, args=(fileName,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

if __name__ == '__main__':
    if os.path.isdir(input_doc_path):
        main()
