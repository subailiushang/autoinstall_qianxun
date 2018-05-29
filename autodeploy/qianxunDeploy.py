#!/usr/bin/env python
# -*- coding:utf8 -*-
# Function:千寻4.5版本产品单机版自动化安装
# Author: zhangzihao@pachiratech.com
# Data: 2018-05-28

import pexpect
import json
import os

os.chdir("/root/test/")
os.system("tar xf QianXun-4.5.Build7118.tar.gz")
os.chdir("QianXun-4.5.Build7118/")


def auto_deploy():
    with open('/root/test/config.json', 'r') as config:
        conf = json.load(config)
        with open("auto.log", 'wb') as f:
            cmd = "/bin/bash install -l zh_CN "
            deploy = pexpect.spawn(cmd, timeout=180, logfile=f)
            # 请选择需要安装的组件(多个组件之间用逗号隔开，默认全选):
            deploy.expect("请选择需要安装的组件".encode())
            deploy.sendline("7,8")
            # 请输入安装目录(/root/QianXun-4.5):
            deploy.expect("请输入安装目录".encode())
            deploy.sendline(conf["install_dir"])
            # 数据库类型(MySQL):
            deploy.expect("数据库类型".encode())
            deploy.sendline("")
            # 服务器名(127.0.0.1):
            deploy.expect("服务器名".encode())
            deploy.sendline("")
            # 端口号(3306):
            deploy.expect("端口号".encode())
            deploy.sendline("")
            # 数据库名(psae40):
            deploy.expect("数据库名".encode())
            deploy.sendline(conf["database"])
            # 用户名:
            deploy.expect("用户名".encode())
            deploy.sendline(conf["mysql_root"])
            # 密码:
            deploy.expect("密码".encode())
            deploy.sendline(conf["mysql_password"])
            # 单点登陆系统外网地址(127.0.0.1):
            deploy.expect("单点登陆系统外网地址".encode())
            deploy.sendline(conf["ip"])
            # 单点登陆系统外网端口(8184):
            deploy.expect("单点登陆系统外网端口".encode())
            deploy.sendline("")
            # 单点登录系统内网地址:
            deploy.expect("单点登录系统内网地址".encode())
            deploy.sendline(conf["ip"])
            # 单点登录系统内网端口(8184):
            deploy.expect("单点登录系统内网端口".encode())
            deploy.sendline("")
            # Optimus识别服务子网网卡IP(127.0.0.1):
            deploy.expect("Optimus识别服务子网网卡IP".encode())
            deploy.sendline(conf["ip"])
            # offsr-threads(16):
            deploy.expect("offsr-threads")
            deploy.sendline(conf["threads"])
            # PSAE服务外网访问地址(127.0.0.1):
            deploy.expect("PSAE服务外网访问地址".encode())
            deploy.sendline(conf["ip"])
            # PSAE服务工作端口(8181):
            deploy.expect("PSAE服务工作端口".encode())
            deploy.sendline("")
            # DC服务地址(127.0.0.1):
            deploy.expect("DC服务地址".encode())
            deploy.sendline(conf["ip"])
            # DC服务端口(8182):
            deploy.expect("DC服务端口".encode())
            deploy.sendline("")
            # Optimus资源管理服务子网网卡IP(127.0.0.1):
            deploy.expect("Optimus资源管理服务子网网卡IP".encode())
            deploy.sendline(conf["ip"])
            # Optimus授权中心地址(127.0.0.1):
            deploy.expect("Optimus授权中心地址".encode())
            deploy.sendline(conf["ip"])
            # Optimus授权中心端口(9999):
            deploy.expect("Optimus授权中心端口".encode())
            deploy.sendline("")
            # 文本数据源探测目录(data-source/text):
            deploy.expect("文本数据源探测目录".encode())
            deploy.sendline("")
            # 语音数据源探测目录(data-source/speech):
            deploy.expect("语音数据源探测目录".encode())
            deploy.sendline("")
            # 请确认您的安装参数，开始安装请输入y，退出请输入n(Y/n):
            deploy.expect("请确认您的安装参数".encode())
            deploy.sendline("Y")
            deploy.expect(["正在安装".encode(), pexpect.EOF])
            print("----------------开始安装-------------------")
