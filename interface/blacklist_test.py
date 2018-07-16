import requests
import unittest
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import blacklist_test_data
from base_case import BaseCase


class BlackListTest(BaseCase):

    def test_add_blacklist(self):
        """添加黑名单"""

        url = 'http://localhost:9090/m4m/action/internetControlAction/add'
        payload = {'type': 2, 'name': '斗鱼', 'url': 'www.douyu.com'}

        self.result = self.session.post(url, payload).json()
        # print(self.result)

        self.assertEqual(self.result['code'], '10000')
        self.assertEqual(self.result['text'], '操作成功')

    def test_delete_blacklist(self):
        """删除测试黑名单1"""

        url = 'http://localhost:9090/m4m/action/internetControlAction/deleteByIds?type=2'
        payload = {'ids': '8f912bb0d34111e7adfb330c633a3472'}

        self.result = self.session.post(url, payload).json()
        # print(self.result)

        self.assertEqual(1, self.result['status'])
        self.assertEqual('10004', self.result['code'])
        self.assertEqual('操作成功', self.result['text'])

    @unittest.skip
    def test_zdelete_all_blacklist(self):
        """删除所有黑名单"""

        url = 'http://localhost:9090/m4m/action/internetControlAction/deleteByIds?type=2'
        payload = {'ids': '8f912bb0d34111e7adfb330c633a347a,8f912bb0d34111e7adfb330c633a3471,'
                          '8f912bb0d34111e7adfb330c633a3473,cc354439026711e884fb0b8f9c77ae9a'}

        self.result = self.session.post(url, payload).json()
        # print(self.result)

        self.assertEqual(1, self.result['status'])
        self.assertEqual('10004', self.result['code'])
        self.assertEqual('操作成功', self.result['text'])

    def test_edit_blacklist(self):
        """编辑测试黑名单2"""

        url = 'http://localhost:9090/m4m/action/internetControlAction/updateById'
        payload = {'id': '8f912bb0d34111e7adfb330c633a3473', 'isDelete': '0', 'name': '新的黑名单名称', 'sendType': '1',
                   'status': '0', 'status1': '0', 'type': '2', 'url': 'm.jd.com'}

        self.result = self.session.post(url, payload).json()
        # print(self.result)
        self.assertEqual(1, self.result['status'])
        self.assertEqual('10003', self.result['code'])
        self.assertEqual('操作成功', self.result['text'])

    def test_query_blacklist_name_null(self):
        """名称为空点击查询"""

        url = 'http://localhost:9090/m4m/action/internetControlAction/selectByParams?icType=2'
        payload = {'order': 'asc', 'offset': 1, 'limit': 10}

        self.result = self.session.post(url, payload).json()
        # print(self.result['result'][0]['name'])

        self.assertEqual('10000', self.result['code'])
        self.assertEqual('操作成功', self.result['text'])
        self.assertEqual(1, self.result['status'])
        self.assertEqual('百度', self.result['result'][0]['name'])
        self.assertEqual('京东', self.result['result'][1]['name'])

    def test_query_blacklist_name_error(self):
        """黑名单名称或网址错误查询"""

        url = 'http://localhost:9090/m4m/action/internetControlAction/selectByParams?icType=2'
        payload = {'order': 'asc', 'offset': 1, 'limit': 10, 'text': '不存在的黑名单或网址名称'}

        self.result = self.session.post(url, payload).json()
        # print(self.result)

        self.assertEqual('10000', self.result['code'])
        self.assertEqual(0, self.result['total'])
        self.assertEqual([], self.result['result'])

    def test_query_blacklist_name_correct(self):
        """名称正确查询"""

        url = 'http://localhost:9090/m4m/action/internetControlAction/selectByParams?icType=2'
        payload = {'order': 'asc', 'offset': 1, 'limit': 10, 'roleName': '百度'}

        self.result = self.session.post(url, payload).json()
        # print(self.result)

        self.assertEqual('百度', self.result['result'][0]['name'])
        self.assertEqual('10000', self.result['code'])
        self.assertEqual(1, self.result['status'])
        self.assertEqual('操作成功', self.result['text'])


    @unittest.skip
    def test_developing_blacklist_strategy(self):
        """下发黑名单策略"""

        url = 'http://localhost:9090/m4m/action/internetControlAction/sendPolicyFile?type=2'
        self.result = self.session.get(url).json()
        # print(self.result)

        self.assertEqual('10000', self.result['code'])
        self.assertEqual(1, self.result['status'])
        self.assertEqual('操作成功', self.result['text'])


    @unittest.skip
    def test_import_blacklist(self):
        """导入黑名单"""
        pass
        # url = 'http://localhost:9090/m4m/action/internetControlAction/batchBlackUpload?type=2'
        # files = {'file': open('web_control.xlsx', 'rb')}
        # self.result = self.session.post(url, files)
        # print(self.result.content)


if __name__ == '__main__':
    blacklist_test_data.init_data()  # 初始化接口测试数据
    unittest.main()
    # 构造测试集
    # suite = unittest.TestSuite()
    # suite.addTest(BlackListTest("test_import_blacklist"))
    #
    # # 执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
