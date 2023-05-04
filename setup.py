from setuptools import setup

setup (
    name='trolleyhq',
    version='1.0.0',
    packages=["trolley", "trolley.exceptions"],
    package_data={"trolley": ["ssl/*"]},
    install_requires=['requests>=2.13.0'],
    author='Trolley',
    author_email='developer-tools@trolley.com',
    summary='Trolley Python SDK',
    url='https://www.trolley.com',
    license='MIT',
    long_description='A native Python SDK for the Trolley API',
)
