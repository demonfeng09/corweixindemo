import sys
import logging
import os
import pytest
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
sys.path.append(os.path.dirname(sys.modules[__name__].__file__))
from initialization import sysconfig

fileHandler = logging.FileHandler(filename="../log/auto.log",encoding="utf-8")
logging.getLogger().setLevel(0)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
fileHandler.setFormatter(formatter)

logging.getLogger().addHandler(fileHandler)

if __name__ == '__main__':
    logging.info("Start to execute automation cases")

    #pytest.main(['testcases/contact/department/test_create_dep.py::TestCreatDep::test_create_new_dep_parm'])
    #pytest.main(['testcases/contact/department/test_update_dep.py'])
    pytest.main(['testcases/contact/member/test_create_member.py::TestCreateMember::test_create_mem_by_data_assert'])
