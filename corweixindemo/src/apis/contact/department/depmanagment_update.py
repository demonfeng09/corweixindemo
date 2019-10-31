from apis.baseapi import BaseAPI
import requests
import logging
from initialization.sysconfig import sys_cfg

class DeptManagment_Update(BaseAPI):

    def __init__(self):
        BaseAPI.__init__(self)
        logging.info("Init department update management API")
        self.update_dep_url = sys_cfg.get('contact_para','update_dep_url')
        self.secret_id = sys_cfg.get('contact_para','secret_id')
        self.dept_id = sys_cfg.get('eightclass_para','dept_id')

    def update_dept(self):
        up_part = {
           "id": self.dept_id,
           "name": "八期测试部20191023",
           "parentid": 1,
           "order": 1
        }

        param_update = {'access_token':self.get_token(self.secret_id)}
        self.post_json(self.update_dep_url,up_part,param_update)

    def get_update_dep_res(self):
        return self.get_response()