#!/usr/bin/python2
# testing qr code decode functionality with qrtools library
# https://github.com/primetang/qrtools

import qrtools
import urllib
import sys
import tempfile

url = sys.argv[1]

# generate a random named file in the tmpdir location
tf = tempfile.NamedTemporaryFile()
tf.name # this is the absolute path to the tmp filename

img = urllib.urlretrieve(url, tf.name) 

# let the module do its thing, the tempfile will be autocleaned up after the script is finished executing. 
qr = qrtools.QR()
qr.decode(tf.name)
print qr.data
