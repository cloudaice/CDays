# -*- coding: utf-8 -*-
import sys
import cmd
from cdctools import *
class PYCDC(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.CDROM='/media/cdrom0'
        self.CDDIR='cdc/'
        self.prompt='(pycdc)>'
        self.intro='''PYCDC0.5使用说明：
        dir       目录名     指定保存目录或者搜索目录 默认是'cdc/'
        walk      文件名     使用"*.cdc" 将扫描得到的目录放到该文件夹中
        find      关键字     搜索遍历目录中的.cdc文件输出含有关键字的行
        diskdir   目录名     指定要扫描的路径名和光盘名 默认是"/media/cdrom0"
        ?         查询帮助
        exit      退出系统
        '''

        
    def help_exit(self):
        print '退出程序 quits the program'

    def do_exit(self,line):
        sys.exit()
    

    def help_diskdir(self):
        print "指定要扫描的光盘路径名以及光盘名"

    def do_diskdir(self,diskdir):
        if diskdir=='': 
            diskdir=raw_input("输入路径名及光盘名\n")
        print "您输入的光盘名及路径名是 %s" % diskdir
        self.CDROM=diskdir


    def help_walk(self):
        print "扫描光盘内容 walk cd and export into *.cdc"

    def do_walk(self,filename):
        if filename=="":
            filename= raw_input("输入文件名:cdc:: ")
        print "扫描光盘内容保存到:'%s'" % filename
        cdwalker(self.CDROM,self.CDDIR+filename)


    def help_dir(self):
        print "指定保存/搜索目录"

    def do_dir(self,pathname):
        if pathname=="":
            pathname=raw_input("输入指定保存/搜索目录:")
        print "指定保存搜索目录是 ‘%s';默认是：'%s'" % (pathname,self.CDDIR)
        self.CDDIR=pathname


    def help_find(self):
        print "搜索关键字"

    def do_find(self,keyword):
        if keyword=="":
            keyword=raw_input("输入搜索关键字:")
        print "搜索关键词: '%s'" % keyword
        cdcgrep(self.CDDIR,keyword)

    do_q=do_exit


if __name__== '__main__':
    cdc=PYCDC()
    cdc.cmdloop()
