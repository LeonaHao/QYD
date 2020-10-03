# -*- coding:utf-8 -*
# @author 190360
"""【前台】分期贷列表查询"""
from Config import openloan_url
from lib.qyd_common import qydFrontLogin
import unittest
import requests
import json
from lib.log import logger
from lib.generateTestCases import __generateTestCases


class fqdList(unittest.TestCase):
    u"""【前台】分期贷列表查询 --张建楠"""
    def setUp(self):
        logger.info("qyd_openloan case is start to run ")

    def getTest(self,testdata):

        headers = {"Content-type": "application/json"}
        if testdata["flag"]==1:
            tel_num = json.loads(testdata['X-Auth-Token'])['tel_num']
            headers["X-Auth-Token"] = qydFrontLogin(tel_num, "che001")
        info=json.JSONDecoder().decode(testdata['params'])
        requests.packages.urllib3.disable_warnings()
        r = requests.post(openloan_url.fqdList, headers=headers, json=info,verify=False)
        result=r.json()
        if str(result["successful"]) ==str(True):
            result_hasCompleted=json.loads(testdata['code'])['hasCompleted']
            self.assertEqual(str(result["entities"][0]['hasCompleted']),str(result_hasCompleted))
            result_hasBankCardInfo = json.loads(testdata['code'])['hasBankCardInfo']
            self.assertEqual(str(result["entities"][0]['hasBankCardInfo']), str(result_hasBankCardInfo))
            print(testdata["test_name"],"\n预期结果：\n",testdata["remark"],"\n实际结果:\n",result["entities"][0])
        else:
            self.assertEqual(str(result["resultCode"]["code"]), str(testdata["code"]))
            print(testdata["test_name"],"\n预期结果：\n",testdata["remark"],"\n实际结果:\n",result["resultCode"]["message"])

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("qyd_openloan case is end to run ")

#类名称，用例别名，数据文件名，sheet名称
__generateTestCases(fqdList,"fqdList","openloan.xlsx","fqdList")

if __name__ == "__main__":
    unittest.main(verbosity=1)

