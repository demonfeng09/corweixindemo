from apis.contact.member.membermanagment import MemberManage
from untils import toolskit
from untils.comparator import JsonComparator

class TestCreateMember():

    '''
        最简单最常规的断言
    '''
    def test_create_mem(self):
        member_creat = MemberManage()
        member_creat.create_member('testdata/contact/member/member.json')
        res = member_creat.get_response()
        print("res========="+res.get('errmsg'))
        assert res.get('errmsg') == 'created'

    '''
        获取一个文件里有多个测试数据的断言
    '''
    def test_create_mem_by_json_obj(self):
        member_json_obj = MemberManage()
        json_obj = member_json_obj.get_multi_member('testdata/contact/member/member2.json','testcase1')
        member_json_obj.create_member_by_json_object(json_obj)
        res = member_json_obj.get_response()
        print("res=========" + res.get('errmsg'))
        assert res.get('errmsg') == 'created'

    '''
        将断言内容参数化
    '''
    def test_create_men_by_parm_json(self):
        member_Param = MemberManage()
        param_json_object = member_Param.get_multi_member('testdata/contact/member/member3.json','testcase1')
        req_param_json = param_json_object.get("req")
        res_param_json_data = param_json_object.get("res")
        member_Param.create_member_by_json_object(req_param_json)
        res_param = member_Param.get_response()
        assert res_param.get('errmsg') == res_param_json_data.get("errmsg")


    '''
        测试数据能实时变更不会重复
    '''
    def test_create_mem_by_data_update(self):
        member_data_update = MemberManage()
        update_json_object = member_data_update.get_multi_member_param('testdata/contact/member/member3.json','testcase1')
        req_param_json_update = update_json_object.get("req")
        res_param_json_update = update_json_object.get("res")
        print(type(res_param_json_update))
        userid = toolskit.append_time_stamp_string(req_param_json_update.get("userid"))
        mobile = toolskit.get_random_mobile()
        email = toolskit.get_random_email()
        toolskit.update_json_value_by_key(req_param_json_update,'userid',userid)
        toolskit.update_json_value_by_key(req_param_json_update, 'mobile', mobile)
        toolskit.update_json_value_by_key(req_param_json_update, 'email', email)

        member_data_update.create_member_by_json_object(req_param_json_update)
        res_param = member_data_update.get_response()
        assert res_param.get('errmsg') == res_param_json_update.get("errmsg")



    '''
        测试数据能实时变更不会重复并且将断言也参数化
    '''
    def test_create_mem_by_data_assert(self):
        member_data_update = MemberManage()
        req_update_json_object = member_data_update.get_multi_member_param('testdata/contact/member/member3.json','testcase1','req')
        std_res_update_json_object = member_data_update.get_multi_member_param('testdata/contact/member/member3.json','testcase1', 'res')

        userid = toolskit.append_time_stamp_string(req_update_json_object.get("userid"))
        mobile = toolskit.get_random_mobile()
        email = toolskit.get_random_email()
        toolskit.update_json_value_by_key(req_update_json_object,'userid',userid)
        toolskit.update_json_value_by_key(req_update_json_object, 'mobile', mobile)
        toolskit.update_json_value_by_key(req_update_json_object, 'email', email)

        member_data_update.create_member_by_json_object(req_update_json_object)
        live_res_param = member_data_update.get_response()
        comparator = JsonComparator()
        assert comparator.equals(live_res_param,std_res_update_json_object)









