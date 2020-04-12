#! /usr/bin/python3.7
# -*- coding: utf-8 -*-

# Author: Andrii Valchuk

from wand.image import Image as wimg
from progress.bar import IncrementalBar

pdfsource = input("Enter source pdf file: ")
imgresolution = int(input("Enter resolution by output images: "))

print("Read pdf file, pleas wait...")

try:
    pdf = wimg(filename=pdfsource, resolution=imgresolution)
    pdfimage = pdf.convert("jpeg")
    imgsequence = pdfimage.sequence
    bar = IncrementalBar('Convert', max = len(imgsequence))
    i = 1
    for img in imgsequence:
        bar.next()
        page = wimg(image=img)
        page.save(filename=str(i)+".jpg")
        i += 1
    bar.finish()
    print("Finish\n")
except PolicyError as ex:
    print('Pdf extraction forbidden by Imagemagick policy: %s', ex)
except Exception as ex:
    print('Cannot extract image: %s', ex)
