#!/usr/bin/python
#-*- coding:utf-8 -*-
import os
import sys
from optparse import OptionParser
#my libs
import const_string

const_version = """    pygen v0.1.0000
    %s
""" % const_string.copyleft  #TODO:[用户友好:version应该自动在发布egg的时候生成，才是对用户负责的]
const_usage = """pygen [options]... [name]
Example:"""

def pygen():
    opt = OptionParser(const_usage)
    opt.add_option('-v', '--version', action="store_true", dest='version')
    (options, args) = opt.parse_args()

    if options.version:
        print const_version;
        return True

if "__main__" == __name__:
    pygen()
    pass
