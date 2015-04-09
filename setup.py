# -*- encoding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='ddshape',
    version='0.1',
    packages=find_packages(),

    package_data={
        'ddshape': ['Template/*.tpl']
    },

    author='Xing',
    author_email='1281961491@qq.com',
    url='https://github.com/xingtingyang/ddshape',
    license='BSD style',
    description='This is a package that can be used to create shape.dat needed by ddscat.'

)