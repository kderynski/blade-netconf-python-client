# Copyright 2010 Blade Network Technologies

import os, sys, string

from bnclient import bnclient 

def str2argv(str=''):
    return str.split(' ')

if __name__ == '__main__':
    # username and password
    options = "-u admin -p admin "
    # hostname
    options += "192.168.237.10"
    
    argv = sys.argv[:1] + str2argv(options) + sys.argv[1:]
    
    bnc = bnclient.bnclient(argv)
    bnc.connect()
    bnc.sendhello()
    bnc.sendrpc(str2argv("-o lock -t running"))
    bnc.sendrpc(str2argv("-o get"))
    bnc.sendrpc(str2argv("-o unlock -t running"))
    bnc.close()
