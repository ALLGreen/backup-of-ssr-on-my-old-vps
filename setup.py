import codecs
from setuptools import setup, find_packages


with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="my-shadowsocksR",
    version="1.0.0",
    license='http://www.apache.org/licenses/LICENSE-2.0',
    description="base on shadowsocksR on my old vps for self use",
    author='allgreen',
    url='https://github.com/ALLGreen/backup-of-ssr-on-my-old-vps',
    packages=find_packages(),
    package_data={
        'shadowsocks': ['README.rst', 'LICENSE']
    },
    install_requires=[],
    entry_points="""
    [console_scripts]
    sslocal = shadowsocks.local:main
    ssserver = shadowsocks.server:main
    """,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: Proxy Servers',
    ],
    long_description=long_description,
)
