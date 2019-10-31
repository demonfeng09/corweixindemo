
import time
import random
import logging
import json


def update_json_value_by_key(json_obj,key,new_value):
    json_obj[key] = new_value
    return json_obj

def append_time_stamp_string(old_value):
    return old_value+"_"+time.strftime('%Y%M%d%H%M%S')

def get_random_mobile():
    list = ['139','188','185','136','155','135','158','152','153']
    str_num = '0123456789'
    mobile_num = random.choice(list)+"".join(random.choice(str_num) for i in range(8))
    logging.info("mobile_num==="+mobile_num)
    return mobile_num


def get_random_email():
    emailtype = ["@qq.com", "@163.com", "@126.com", "@189.com"]
    email_str_ran = '0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ'
    random_number = "".join(random.choice(email_str_ran) for i in range(5))
    random_type = random.choice(emailtype)
    email = random_number+random_type
    logging.info("email===="+email)
    return email

def get_dict_value():
    res = {
        "errcode": "0",
        "errmsg": "created"
    }
    print(type(res))
    b = json(res)
    print(type(b))
    print(b)
    a = res.get("errcode")
    c = b[0][0]
    print(c)

if __name__ == '__main__':
    get_dict_value()