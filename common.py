import collections
import os.path

#0,0 is top left

outsize = (826,1705,3)

regions = collections.OrderedDict()
#fmt:(h,w),(desty,destx),borderw,(text,texty,textx)
regions["foo"] =     ((768,1024),(50,2),1,("A Large Image",50-12,10))
regions["bar"] =   ((494,659),(50,1040),1,("Medium",50-12,1045))
regions["baz"] =  ((76,321),(768+50-76-4,6),1,("Inset",768+50-76-10-12,10))
regions["bob"] =   ((215,390),(768+50-215,1040),1,("Another",768+50-215-12,1045))

idir = os.environ.get("IDIR","imgs")+"/"
odir = os.environ.get("ODIR","frames")+"/"

fps = 10.0
dt = 1.0/fps

bordercolor = (0,0,0)
textcolor = (0, 0, 0)

if not os.path.exists(idir):
    os.makedirs(idir)

if not os.path.exists(odir):
    os.makedirs(odir)
