qrcode_scripts
==============
### How to use:
###### decode_qrcode.py

##### first argument of the script can be a URL to an existing qr code img
```
python2 decode_qrcode.py "http://cdn4.explainthatstuff.com/qr-code-barcode-example-ets.png"
http://www.explainthatstuff.com/
```

##### first argument of the script can also be a file existing on the system already. 
```
wget "http://cdn4.explainthatstuff.com/qr-code-barcode-example-ets.png" -O example_qrcode.png 2> /dev/null

file example_qrcode.png 
example_qrcode.png: PNG image data, 248 x 248, 8-bit colormap, non-interlaced

python2 decode_qrcode.py example_qrcode.png 
http://www.explainthatstuff.com/
```
