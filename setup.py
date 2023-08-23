from setuptools import setup, find_packages
from pathlib import Path

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 11',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf8') + '\n\n' + (this_directory / "CHANGELOG.md").read_text(encoding='utf8')

setup(
  name='banknatchapolfunctions',
  version='0.1.3',
  description='ฟังก์ชันของ Bank Natchapol',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='',  
  author='Bank Natchapol',
  author_email='natchapol.pat@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='banknatchapol', 
  packages=find_packages(),
  install_requires=['numpy', 'pandas', 'matplotlib'] 
)