from setuptools import setup

setup (
    name='trolleyhq',
    version='1.1.0',
    packages=["trolley", "trolley.exceptions", "trolley.utils", "trolley.types", "paymentrails"],
    package_data={"trolley": ["ssl/*"]},
    install_requires=['requests>=2.32.0'],
    python_requires='>=3.9',
    author='Trolley',
    author_email='developer-tools@trolley.com',
    description='Trolley Python SDK',
    url='https://www.trolley.com',
    license='MIT',
    long_description='A native Python SDK for the Trolley API',
)
