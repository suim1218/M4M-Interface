import requests
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import role_test_data
from base_case import BaseCase


class NoticeTest(BaseCase):

    # @unittest.skip
    def test_add_role(self):
        """添加角色"""

        url = 'http://localhost:9090/m4m/action/roleAction/insertRole'
        payload = {'name': '测试角色4'}

        self.result = self.session.post(url, payload).json()
        # print(self.result)

        self.assertEqual(self.result['code'], '10000')
        self.assertEqual(self.result['text'], '操作成功')
        self.assertEqual(self.result['status'], 1)


if __name__ == '__main__':
    role_test_data.init_data()  # 初始化接口测试数据
    unittest.main()
