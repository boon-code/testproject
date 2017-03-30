from setuptools import setup
import datetime

YEAR = datetime.date.today().year

__author__ = "Manuel Huber"
__docformat__ = "restructuredtext en"


setup( name = 'pkg1'
     , version_format = "{tag}.dev{commitcount}+{gitsha}"
     , description = 'First package'
     , author = __author__
     , author_email = 'Manuel.h87@gmail.com'
     , url = 'https://github.com/boon-code'
     , classifiers = [ "Development Status :: 2 - Pre-Alpha"
                     , "License :: OSI Approved :: MIT License"
                     , "Programming Language :: Python :: 2.7"
                     , "Programming Language :: Python :: 3"
                     ]
     , packages = ['../common', 'pkg1']
     , setup_requires = [ "setuptools>=8.0"
                        , "setuptools-git-version>=1.0.3"
                        ]
     , install_requires = []
     , entry_points = {
           'console_scripts' :
               [ 'first = pkg1.__init__:main'
               ]
       }
     )
