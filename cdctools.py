# -*- coding:utf-8 -*-
import os
import sys
import chardet
def cdwalker(cdrom,cdfile):
    export=""
    for root,dirs,files in os.walk(cdrom):
        export+=formatinfo(root,dirs,files)
    open(cdfile,"w").write(export)

def cdcgrep(filepath,keyword):
    filelist=os.listdir(filepath)
    for cdc in filelist:
        if '.cdc' in cdc:
            cdcfile=open(filepath+cdc)
            for line in cdcfile.readlines():
                if keyword in line:
                    print line

def _smartcode(stream):
    """smart stream into utf-8"""
    codedetect = chardet.detect(stream)["encoding"]
    ustring = unicode(stream,codedetect)
    return ustring.encode('utf-8')
    
def formatinfo(root,dirs,files):
    export = "\n"+root+"\n"
    for d in dirs:
        export+="-d %s %s \n" % (root,_smartcode(d))
    for f in files:
        export+="-f %s %s \n" % (root,_smartcode(f))
    export+= "="*100
    return export

if __name__ == '__main__':
    cdwalker("/media/cdrom0",'s.cdc')
