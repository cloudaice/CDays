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
        dir 目录名 #指定保存目录和搜索目录名 默认是'cdc'
        walk 文件名 使用"*.cdc"
        find 关键字  搜索遍历目录中左右.cdc文件输出含有关键字的行
        ? 查询
        exit 推出系统
        '''

        
    def help_exit(self):
        print '推出程序 quits the program'
    def do_exit(self,line):
        sys.exit()
    
    def help_walk(self):
        print "扫描光盘内容 walk cd and export into *.cdc"
    def do_walk(self,filename):
        if filename=="": filename= raw_input("输入文件名:cdc::")
        print "扫描光盘内容保存到:'%s'" % filename
        cdwalker(self.CDROM,self.CDDIR+filename)

    def help_dir(self):
        print "指定保存/搜索目录"
    def do_dir(self,pathname):
        if pathname=="":pathname=raw_input("输入指定保存/搜索目录:")
        self.CDDIR=pathname
        print "指定保存搜索目录是 ‘%s';默认是：'%s'" % (pathname,self.CDDIR)

    def help_find(self):
        print "搜索关键字"
    def do_find(self,keyword):
        if keyword=="":keyword=raw_input("输入搜索关键字:")
        print "搜索关键词: '%s'" % keyword
        cdcgrep(self.CDDIR,keyword)
if __name__== '__main__':
    cdc=PYCDC()
    cdc.cmdloop()
