[TOC]

# 安装
pip install pipenv

# 显示目前的环境目录

pipenv --venv

# 安装环境
pipenv --three
--three代表以python3为基础，--two是python2

# 启动环境

pipenv shell

# 安装第三方库
pipenv install django

# 退出环境
exit

# 查看解释器目录
pipenv --py

# 查看包依赖关系

pipenv graph

# 卸载第三方库
pipenv uninstall requests

# 卸载所有库
pipenv uninstall --all

# 在虚拟环境下运行脚本
pipenv run python test.py

# 删除环境
pipenv --rm

会在C:\Users\glzha\.virtualenvs\这个目录下生成虚拟环境相关配置文件