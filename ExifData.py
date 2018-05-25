#!/usr/bin/env python

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlsplit
from os.path import basename
from PIL import Image
from PIL.ExifTags import TAGS
import argparse


def fineImages(url):
    print ('[ * ] Finding images on: ' +url)
    urlcontent = urlopen(url)
    soup = BeautifulSoup(urlcontent)
    imgTags = soup.find_all('img')
    return imgTags

def downloadImg(imgTag):
    try:
        print('[+] Downloading Image..')
        imgSrc = imgTag['src']
        imgContent = urlopen(imgSrc).read()
        imgFileName = basename(urlsplit(imgSrc)[2])
        imgFile = open(imgFileName,'wb')
        imgFile.write(imgContent)
        imgFile.close()
        return imgFileName
    except:
        return ''
def testforExif(imgFileName):
    try:
        exifData = {}
        imgFile = Image.open(imgFileName)
        info = imgFile._getdata()
        if info:
            for (value, tag) in info.items():
                decoded = TAGS.get(tag, tag)
                exifData[decoded] = value
            exifGPS = exifData['GPSInfo']
            if exifGPS:
                print('[*]' + imgFileName + 'Contains GPS information')
    except:
        pass

def main():
    parser = argparse.ArgumentParser(prog='ExifData',usage='-u tatgeturl')
    parser.add_argument('-u','--url',help='The url to be checked',type=str)
    args = parser.parse_args()
    url = args.url
    if url == None:
        print(parser.prog + parser.usage)
        exit(0)
    else:
        imgTags = fineImages(url)
        for imgTag in imgTags:
            imgFileName = downloadImg(imgTag)
            testforExif(imgFileName)

if __name__ == '__main__':
    main()