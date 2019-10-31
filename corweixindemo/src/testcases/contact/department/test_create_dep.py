from apis.contact.department.depmanagment import DeptManagment
import pytest

class TestCreatDep:

    def test_create_new_dep(self):
        dept_managment = DeptManagment()
        dept_managment.creat_dept()
        create_res = dept_managment.get_response()
        assert create_res.get('errmsg') == 'created'

    @pytest.mark.parametrize("name",["测试部","产品部","财务部"])
    def test_create_new_dep_parm(self,name):
        dept_managment = DeptManagment()
        dept_managment.creat_dept_param(name)
        create_res = dept_managment.get_response()
        assert create_res.get('errmsg') == 'created'