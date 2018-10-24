from setuptools import setup

setup (
    name='paymentrails',
    version='0.1',
    packages=["paymentrails", "paymentrails.exceptions"],
    package_data={"paymentrails": ["ssl/*"]},
    install_requires=['requests>=2.13.0'],
    author='Jesse',
    author_email='jesse.silber@paymentrails.com',
    summary='Payment Rails Python SDK',
    url='',
    license='',
    long_description='A native Python SDK for the Payment Rails API',
)
