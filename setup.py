from setuptools import setup

setup(
    name='shotty',
    version='0.1',
    author='Ian Johnson',
    author_email='tacoda@pm.me',
    description='Shotty is a tool to manage AWS EC2 snapshots',
    license='GPLv3+',
    packages=['shotty'],
    url='https://gitlab.com/tacoda/shotty',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    '''
)
