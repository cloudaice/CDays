#-*- cding:utf-8 -*-
import os
for root,dirs,files in os.walk("/media/cdrom0"):
    open("mydoc.cdc",'a').write("%s %s %s" %(root,dirs,files))
