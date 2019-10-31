from apis.baseapi import BaseAPI
import logging
from initialization.sysconfig import sys_cfg
import codecs
import json
import pytest

class DeptManagment(BaseAPI):

    def __init__(self):
        BaseAPI.__init__(self)
        logging.info("Init department management API")
        self.create_dep_url = sys_cfg.get('contact_para','creat_dep_url')
        self.secret_id = sys_cfg.get('contact_para','secret_id')
        self.dept_id = sys_cfg.get('eightclass_para','dept_id')

    def creat_dept(self):
        new_part = {
           "name": "八期测试部",
           "parentid": 1,
           "order": 1,
        }
        params = {'access_token':self.get_token(self.secret_id)}
        self.post_json(self.create_dep_url,new_part,params)

    def creat_dept_param(self,name):
        new_part = {
            "name": name,
            "parentid": 1,
            "order": 1,
        }
        params = {'access_token': self.get_token(self.secret_id)}
        self.post_json(self.create_dep_url, new_part, params)

    def get_create_dept_res(self):
        return self.get_response()









