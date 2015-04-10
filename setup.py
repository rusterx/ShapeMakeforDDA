# -*- encoding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='ddshape',
    version='0.11',
    packages=find_packages(),

    package_data={
        'ddshape': ['Template/*.tpl']
    },

    author='Xing',
    author_email='1281961491@qq.com',
    url='https://github.com/xingtingyang/ddshape',
    license='BSD style',
    long_description=open('README.md').read()

)