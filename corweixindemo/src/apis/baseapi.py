import logging
import requests
from initialization.sysconfig import sys_cfg
import codecs
import json
import pytest

class BaseAPI:

    def __init__(self):
        logging.info("init base api interfase")
        self.cop_id = sys_cfg.get('corp_para','corpid')
        self.token_url = sys_cfg.get('corp_para','token_url')
        self.get_res = ''

    def get_token(self,secret):
        params = {'corpid':self.cop_id,'corpsecret':secret}
        res = requests.get(self.token_url,params=params,verify=False)
        return res.json().get('access_token')

    def post_json(self,url,json_obj,params=None):
        if params:
            self.get_res = requests.post(url,json=json_obj,params=params)
        else:
            self.get_res = requests.post(url, json=json_obj)

    def get_response(self):
        return self.get_res.json()

    '''
        一个文件里只有一个测试数据---member.json
    '''
    def get_new_member(self, filename):
        with codecs.open(filename, 'r', encoding='utf8') as f:
            json_object = json.loads(f.read(), encoding='utf8')
            logging.debug("json_object====" + str(json_object))
            print("json_object====" + str(json_object))
            return json_object

    '''
        一个文件里有多个测试数据---member2.json/member3.json 位置放的不合理
    '''
    def get_multi_member(self,filename,testcase_name):
        with codecs.open(filename,'r',encoding='utf8') as f:
            multipy_json_obj = json.loads(f.read(),encoding='utf8')
            test_case_name_json_obj = multipy_json_obj.get(testcase_name)
            return  test_case_name_json_obj


'''
    #pip install datafiles
    @pytest.mark.datafiles(
        '../testdata/test1.json'
        '../testdata/test2.json'
    )
    def test_n_files(self,datafiles):
        for member_file in datafiles.listdir():
            return
'''