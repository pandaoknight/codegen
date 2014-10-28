#-*- coding: utf-8 -*-
from namegen import namegen


def gen_php_router(name):
    n = namegen(name)
    return "'/%s' => '%s'," % (name, n.controller_name())
