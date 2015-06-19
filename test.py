#!/usr/bin/env python
#encoding: utf-8

import unittest

class mytest(unittest.TestCase):
    
    ##初始化工作
    def setUp(self):
        pass
    
    #退出清理工作
    def tearDown(self):
        pass
    
    #具体的测试用例，一定要以test开头
    def testsum(self):
        self.assertEqual('='.join(['o','p']),'o=p')
        
        
        
if __name__ =='__main__':
    unittest.main()
