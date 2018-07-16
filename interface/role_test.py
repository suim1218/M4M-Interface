import requests
import unittest
import os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import role_test_data
from base_case import BaseCase


class RoleTest(BaseCase):

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

    # @unittest.skip
    def test_delete_role(self):
        """删除测试角色3"""

        url = 'http://localhost:9090/m4m/action/roleAction/deleteById'
        payload = {'id': 'a688f753d31411e79e4733a8a18c99a4'}

        self.result = self.session.post(url, payload).json()
        # print(self.result)

        self.assertEqual(self.result['text'], '删除成功')
        self.assertEqual(self.result['status'], 1)
        self.assertEqual(self.result['result'], 1)

    # @unittest.skip
    def test_edit_role(self):
        """编辑测试角色2"""

        url = 'http://localhost:9090/m4m/action/roleAction/updateById'
        payload = {'id': 'a688f753d31411e79e4733a8a18c99a3', 'name': '测试角色2a'}

        self.result = self.session.post(url, payload).json()
        print(self.result)

        self.assertEqual(self.result['text'], '操作成功')
        self.assertEqual(self.result['status'], 1)
        self.assertEqual(self.result['result'], 1)

    # @unittest.skip
    def test_inquire_all_role(self):
        """查询所有角色"""

        url = 'http://localhost:9090/m4m/action/roleAction/selectByParams'
        payload = {'order': 'desc', 'offset': 1, 'limit': 10}

        self.result = self.session.post(url, payload).json()
        print(self.result['result'])
        # self.assertEqual(self.result['result'][1]['name'], '公告发送管理员')
        # self.assertEqual(self.result['result'][2]['name'], '分管理员')

    @unittest.skip
    def test_accurate_inquire_role(self):
        """精确查询角色"""

        url = 'http://localhost:9090/m4m/action/roleAction/selectByParams'
        payload = {'order': 'desc', 'offset': 1, 'limit': 10, 'roleName': '分管理员'}

        self.result = self.session.post(url, payload).json()
        # print(self.result['result'][0]['name'])

        self.assertEqual(self.result['result'][0]['name'], '分管理员')

    # @unittest.skip
    def test_blurry_inquire_role(self):
        """根据关键字员模糊查询"""

        url = 'http://localhost:9090/m4m/action/roleAction/selectByParams'
        payload = {'order': 'desc', 'offset': 1, 'limit': 10, 'roleName': '员'}

        self.result = self.session.post(url, payload).json()
        # print(self.result['result'])

        self.assertEqual(self.result['result'][1]['name'], '公告发送管理员')
        self.assertEqual(self.result['result'][2]['name'], '分管理员')


if __name__ == '__main__':
    role_test_data.init_data()  # 初始化接口测试数据
    # unittest.main()
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(RoleTest("test_inquire_all_role"))


    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
