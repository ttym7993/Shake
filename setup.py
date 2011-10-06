# -*- coding: utf-8 -*-
import os
from setuptools import setup


ROOTDIR = os.path.dirname(__file__)
README = os.path.join(ROOTDIR, 'README.txt')


def run_tests():
    import sys, subprocess
    errno = subprocess.call([sys.executable, 'run_tests.py'])
    raise SystemExit(errno)


setup(
    name='Shake',
    version='0.5.3',
    author='Juan-Pablo Scaletti',
    author_email='juanpablo@lucumalabs.com',
    packages=['shake'],
    package_data={
        'shake': [
            '.gitignore',
            'default_views/*.*',
            'skeleton/app/views/*.*',
            'skeleton/app/*.*',
            'skeleton/static/css/*.*',
            'skeleton/static/images/*.*',
            'skeleton/static/js/*.*',
            'skeleton/static/*.*',
            'skeleton/*.*',
        ]
    },
    zip_safe=False,
    url='http://github.com/lucuma/Shake',
    license='MIT license (http://www.opensource.org/licenses/mit-license.php)',
    description='A web framework mixed from the best ingredients',
    long_description=open(README).read(),
    install_requires=[
        'Werkzeug>=0.7',
        'Jinja2>=2.4',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='__main__.run_tests',
    entry_points="""
    [console_scripts]
    shake = shake.shake_vudu:main
    """
)
