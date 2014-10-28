import os
from string import Template
import template
from namegen import namegen


def gen_php_controller(root, name):
    n = namegen(name)
    s = Template(template.controller)
    d = {}
    d['controller_name'] = n.controller_name()
    d['model_name'] = n.model_name()
    d['view_name'] = 'WanhuiFrameSimpleHtmlView'
    d['tpl_name'] = n.tpl_name()

    target_path = os.path.join(root,'controllers',n.controller_name()+'.php')
    print 'Start generating controller'
    print "\twriting: "+target_path
    f = open(target_path, 'w')
    f.write(s.substitute(d))
    f.close()
    
    return s.substitute(d)

def gen_php_model(root, name):
    n = namegen(name)
    s = Template(template.model)
    d = {}
    d['model_name'] = n.model_name()

    target_path = os.path.join(root,'models',n.model_name()+'.php')
    print 'Start generating model'
    print "\twriting: "+target_path
    f = open(target_path, 'w')
    f.write(s.substitute(d))
    f.close()
    
    return s.substitute(d)

def gen_php_tpl(root, name):
    n = namegen(name)
    s = Template(template.tpl)
    d = {}

    target_path = os.path.join(root,'smarty/templates',n.tpl_name()+'.tpl')
    print 'Start generating tpl'
    print "\twriting: "+target_path
    f = open(target_path, 'w')
    f.write(s.substitute(d))
    f.close()
    
    return s.substitute(d)


if "__main__" == __name__:
    print gen_php_controller('/home/chenxing9/temp_svn_0/svn/trunk/php/ticketcenter/mobile', 'pannad_chen')
    pass
