import time
import random
import os.path
import glob

import cv2.cv
import numpy as np

try:
    import progressbar
except ImportError:
    progressbar = None

from common import regions,idir,odir,fps,dt,textcolor,bordercolor,outsize

def new_frame():
    img = np.zeros(outsize, dtype=np.uint8)
    img.fill(255)
    return img

def get_frame_details(f):
    ts,name = os.path.basename(f).split("_")
    return float(ts),name[0:-4]

def get_frame_data(f):
    img = cv2.imread(f)
    assert img.ndim == 3
    assert img.shape[2] == 3
    return img

def write_frame(last, num, t):
    for n in regions:
        if last[n] is None:
            #no data
            return num

    img = new_frame()
    for n in regions:
        rimg = last[n]
        expectedsize,destloc,borderw,textdetails = regions[n]

        assert expectedsize == rimg.shape[0:2]

        y0,y1 = destloc[0],destloc[0]+rimg.shape[0]
        x0,x1 = destloc[1],destloc[1]+rimg.shape[1]

        for rgbchan in (0,1,2):
            img[y0:y1,x0:x1,rgbchan] = rimg[:,:,rgbchan]

        if borderw > 0:
            cv2.rectangle(img, (x0,y0), (x1,y1), bordercolor, borderw, cv2.CV_AA)

        if textdetails:
            txt,yt,xt = textdetails
            cv2.putText(img, txt, (xt, yt), cv2.FONT_HERSHEY_DUPLEX, 1.0, textcolor, 1, cv2.CV_AA)

    cv2.imwrite("{}/{:0>6d}.png".format(odir,num), img)
    return num+1

lastframes = {k:None for k in regions}


files = glob.glob(idir+"/*.png")
files.sort()

tf = get_frame_details(files[0])[0]
of = 0

if progressbar:
    widgets = [progressbar.Percentage(),progressbar.Bar(), progressbar.ETA()]
    pbar = progressbar.ProgressBar(widgets=widgets,maxval=len(files)).start()
else:
    pbar = None

for num,f in enumerate(files):
    t,n = get_frame_details(f)
    lastframes[n] = get_frame_data(f)
    if (t-tf) > dt:
        of = write_frame(lastframes, of, t)
        tf = t

        if pbar:
            pbar.update(num)
        else:
            print "wrote ",of

if pbar:
    pbar.finish()
