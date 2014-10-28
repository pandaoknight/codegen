#-*- coding:utf-8 -*-
import os


#Data
__all__ = ['check_php_project']

#Function
def check_php_project(root):
    required_dirs = ['controllers', 'models', 'smarty/templates']
    required_files = ['common/InitRouter.php']

    return check(root, required_dirs, required_files)

def check(root, dirs, files):
    print "Checking root is: " + root
    print "Start checking dirs:"
    flag = True
    for dir in dirs:
        target_dir = os.path.join(root, dir)
        if os.path.isdir(target_dir):
            print "\t" + target_dir + " [OK]"
        else:
            print "\t" + target_dir + " [Not Exists]"
            flag = False
    print "Start checking files:"
    for file in files:
        target_file = os.path.join(root, file)
        if os.path.isfile(target_file):
            print "\t" + target_file + " [OK]"
        else:
            print "\t" + target_file + " [Not Exists]"
            flag = False

    return flag


#Inline Test
def __test():
    print check_php_project('/home/chenxing9/temp_svn_0/svn/trunk/php/ticketcenter/mobile')  #绝对路径
    print check_php_project('test/dir')  #相对路径

if '__main__' == __name__:
    __test()
