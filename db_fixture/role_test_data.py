import sys
import time
sys.path.append('../db_fixture')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB


# create data
datas = {
    #角色表
    'sys2_role':[
        {'ROLE_ID': '9f16d542d93011e6abf1f31db9f55f18', 'ROLE_NAME': '超级管理员', 'ROLE_ENABLE': 1, 'ROLE_STATE': 1,
         'RECORD_TYPE': 1},
        {'ROLE_ID': 'send_topic', 'ROLE_CODE':'topic', 'ROLE_NAME': '公告发送管理员', 'ROLE_ENABLE': 1, 'ROLE_STATE': 1,
         'RECORD_TYPE': 1},
        {'ROLE_ID': 'fd605080781a11e7adb429d3474224cc', 'ROLE_NAME': '分管理员', 'ROLE_ENABLE': 1, 'ROLE_STATE': 1,
         'RECORD_TYPE': 1},
        {'ROLE_ID': 'no_role', 'ROLE_NAME': '无', 'ROLE_ENABLE': 1, 'ROLE_STATE': 1, 'RECORD_TYPE': 1},
        {'ROLE_ID': 'a688f753d31411e79e4733a8a18c99a2', 'ROLE_NAME': '测试角色1', 'ROLE_ENABLE': 1, 'ROLE_STATE': 1,
         'RECORD_TYPE': 1},
        {'ROLE_ID': 'a688f753d31411e79e4733a8a18c99a3', 'ROLE_NAME': '测试角色2', 'ROLE_ENABLE': 1, 'ROLE_STATE': 1,
         'RECORD_TYPE': 1},
        {'ROLE_ID': 'a688f753d31411e79e4733a8a18c99a4', 'ROLE_NAME': '测试角色3', 'ROLE_ENABLE': 1, 'ROLE_STATE': 1,
         'RECORD_TYPE': 1},
    ],
}


# Inster table datas
def init_data():
    DB().init_data(datas)


if __name__ == '__main__':
    init_data()
