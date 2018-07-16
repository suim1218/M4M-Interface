import sys
import time
sys.path.append('../db_fixture')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB

now_time = time.strftime("%Y-%m-%d %H:%M:%S")
# print(now_time)

# create data
datas = {
    #公告表
    'bg_notice':[
        {'N_ID': '0c875404d34c11e7adfbb76dbe621186', 'N_TEXT': '测试公告1', 'CREATER_ID': 'e70a3d43d93911e69b110b12326105ff',
         'CREATE_DATE': now_time, 'STATUS1': '0'},
        {'N_ID': '0ed03296d34c11e7adfba3c447b71834', 'N_TEXT': '测试公告2','CREATER_ID': 'e70a3d43d93911e69b110b12326105ff',
         'CREATE_DATE': now_time, 'STATUS1': '0'},


    ],
}


# Inster table datas
def init_data():
    DB().init_data(datas)


if __name__ == '__main__':
    init_data()
