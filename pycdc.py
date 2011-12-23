# -*- coding:utf-8 -*-
import os
import sys
CDROM="/media/cdrom0"
def cdwalker(cdrom,cdfile):
    export=""
    for root,dirs,files in os.walk(cdrom):
        export+="\n %s;%s;%s" %(root,dirs,files)
    open(cdfile,"w").write(export)
if "-e"==sys.argv[1]:
    cdwalker(CDROM,sys.argv[2])
    print"记录被保存在 %s" % sys.argv[2]
else:
    print '''pyCDC使用方法：
    python pycdc.py -e filename
    将光盘内容记录为filename
    '''
