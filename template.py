#-*- coding:utf-8 -*-


controller = '''<?php
require_once(WEB_ROOT . 'controllers/extra/Controller.php');
require_once(WEB_ROOT . 'models/${model_name}.php');
require_once(WEB_ROOT . 'views/HtmlView.php');
require_once(WEB_ROOT . 'views/${view_name}.php');

class ${controller_name} extends Controller {
  public function __construct() {
    $$this->SetResource('${model_name}', '${view_name}', '${tpl_name}.tpl');
  }
}'''


model = '''<?php
require_once(WEB_ROOT . 'models/extra/AbstractSafeModel.php');
require_once(WEB_ROOT . 'models/extra/Response.php');
require_once(WEB_ROOT . 'models/extra/Enums.php');
require_once(WEB_ROOT . 'models/extra/LoginControllModel.php');


class ${model_name} extends LoginControllModel {

    protected $$need_login = false;

    public function GetResult() {
        $$response = new Response();
        $$response->data = array(
            //'mid' => $$this->user_info['memberid']
        );
        return $$response;
    }
}'''

tpl = '''Hello
'''
