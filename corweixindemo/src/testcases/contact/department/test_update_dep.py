from apis.contact.department.depmanagment_update import DeptManagment_Update

class TestUpdateDep:

    update_deptMange = DeptManagment_Update()
    update_deptMange.update_dept()
    update_res = update_deptMange.get_update_dep_res()
    assert update_res.get('errmsg') == 'updated'