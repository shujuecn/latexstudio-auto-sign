#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
'''
@Brief  : LaTeXStudio 自动登录并签到
@Time   : 2022/10/06 20:06:07
@Author : https://github.com/shujuecn
'''

import requests


def login(username, password):
    '''
    @Brief  : 登录
    @Param  : username: 用户名
    @Param  : password: 密码
    @Return : token
    '''

    url = 'https://www.latexstudio.net/api/user/login'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'cookie': ''
    }
    data = {'account': username, 'password': password}

    print("\n正在登录: LaTeX工作室...")

    s = requests.Session()
    response = s.post(url, headers=headers, data=data)

    if response.status_code == 200:
        token = response.json()['data']['userinfo']['token']
        print("登录成功！")
        return token


def sign(token):
    '''
    @Brief  : 签到
    @Param  : token: 登录成功后返回的token
    '''

    url = 'https://www.latexstudio.net/api/Sign/Sign'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'token': f'{token}'
    }

    print("正在签到...")

    s = requests.Session()
    response = s.post(url, headers=headers)

    if response.status_code == 200:
        msg = response.json()['msg']
        print("\033[31m" + msg + "\033[0m\n")


def main():

    username = input('请输入邮箱: ')
    password = input('请输入密码: ')

    token = login(username, password)
    sign(token)


if __name__ == '__main__':
    main()
