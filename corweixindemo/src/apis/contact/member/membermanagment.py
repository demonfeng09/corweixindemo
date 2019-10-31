from apis.baseapi import BaseAPI
from initialization.sysconfig import sys_cfg
import codecs
import json
import logging



class MemberManage(BaseAPI):

    def __init__(self):
        logging.info("Init member management API")
        BaseAPI.__init__(self)
        self.create_member_url = sys_cfg.get('contact_para','create_member_url')
        self.secret_id = sys_cfg.get('contact_para', 'secret_id')



    def create_member(self,filename):
        params = {'access_token': self.get_token(self.secret_id)}
        json_part = self.get_new_member(filename)
        self.post_json(self.create_member_url,json_part,params)

    def create_member_by_json_object(self,json_object):
        params = {'access_token': self.get_token(self.secret_id)}
        self.post_json(self.create_member_url,json_object,params)


    def create_member_response(self):
        return self.get_response()


    '''
        一个文件里有多个测试数据---member2.json/member3.json
    '''
    def get_multi_member_param(self, filename, testcase_name,type):
        with codecs.open(filename, 'r', encoding='utf8') as f:
            multipy_json_obj = json.loads(f.read(), encoding='utf8')
            test_case_name_param = multipy_json_obj.get(testcase_name)
            test_res_or_req_param = test_case_name_param.get(type)
            logging.info(test_res_or_req_param)
            return test_res_or_req_param
