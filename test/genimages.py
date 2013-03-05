import time
import random

import cv2
import numpy as np

from common import idir,regions,fps,dt

colors = ((255,0,0),(0,255,0),(0,0,255))

tn = t0 = time.time()
#make 7s of data
while tn < (t0 + 7.0):
    #each image occurs approximately at 2x the framerate
    tick = random.random()*(dt/len(regions))
    tn = tn + tick

    n = random.choice(regions.keys())
    sz = regions[n][0]

    img = np.zeros((sz[0],sz[1],3), dtype=np.uint8)
    for j,rgb in enumerate(random.choice(colors)):
        img[:,:,j] = rgb

    cv2.putText(img, "%.1f"%tn, (5, 15), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0))

    fn = "%s/%f_%s.png" % (idir,tn,n)
    cv2.imwrite(fn,img)
    
    print "dt = %.1f wrote %s" % (tn-t0, fn)

