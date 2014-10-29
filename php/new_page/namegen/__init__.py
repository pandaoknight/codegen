#-*- coding: utf-8 -*-
import string


class namegen:
    name = ''
    splited_name = []

    def __init__(self, under_score_case):
        self.name = under_score_case.lower()
        self.splited_name = self.name.split('_')

    # 获得标准的命名
    def under_score_case(self):
        return self.name

    def CamelCase(self):
        #TODO
        #g = lambda x: x.capitalize()
        return ''.join(map(lambda x: x.capitalize(), self.splited_name))

    def lowerCamelCase(self):
        #TODO
        return self.splited_name[0]+''.join(map(lambda x: x.capitalize(), self.splited_name[1:]))

    # 业务相关
    def model_name(self):
        return self.CamelCase() + 'Model'

    def controller_name(self):
        return self.CamelCase() + 'Controller'

    def tpl_name(self):
        return self.under_score_case()


if '__main__' == __name__:
    name = namegen('pannad_chen')
    print name.under_score_case()
    print name.lowerCamelCase()
    print ''

    print name.model_name()
    print name.controller_name()
    print name.tpl_name()
    pass
