from setuptools import setup

setup (
    name='paymentrails',
    version='0.2',
    packages=["paymentrails", "paymentrails.exceptions"],
    package_data={"paymentrails": ["ssl/*"]},
    install_requires=['requests>=2.13.0'],
    author='Trolley',
    author_email='developer-tools@trolley.com',
    summary='Trolley Python SDK',
    url='',
    license='',
    long_description='A native Python SDK for the Trolley API',
)
