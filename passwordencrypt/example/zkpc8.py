# coding: utf-8
# author: QCL
# software: PyCharm Professional Edition 2018.2.8
"""
爱应用登录'pwd'加密参数破解
url：http://www.iappstoday.com/
"""
import os
from passwordencrypt.utils import get_execjs_instance


current_filename = os.path.basename(__file__)
js_filename = get_execjs_instance.get_js_filename(current_filename)
ctx = get_execjs_instance.get_ctx_obj(js_filename)


password = "666666"
js_pattern = 'get_password("{}")'.format(password)
print(ctx.eval(js_pattern))