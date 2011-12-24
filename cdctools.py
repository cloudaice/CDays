# -*- coding:utf-8 -*-
import os
import sys
def cdwalker(cdrom,cdfile):
    export=""
    for root,dirs,files in os.walk(cdrom):
        export+="\n %s;%s;%s" %(root,dirs,files)
    open(cdfile,"w").write(export)

def cdcgrep(filepath,keyword):
    filelist=os.listdir(filepath)
    for cdc in filelist:
        if '.cdc' in cdc:
            cdcfile=open(filepath+cdc)
            for line in cdcfile.readlines():
                if keyword in line:
                    print line
if __name__ == '__main__':
    CDROM="/media/cdrom0"
    
