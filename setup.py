from distutils.core import setup

with open('README.rst', encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name='nornir_pygnmi',
  packages=['nornir_pygnmi', 'nornir_pygnmi.tasks'],
  version='0.2.0',
  license='bsd-3-clause',
  description='pyGNMI plugin for Nornir.',
  long_description=long_description,
  long_description_content_type='text/x-rst',
  author='Anton Karneliuk',
  author_email='anton@karneliuk.com',
  url='https://github.com/akarneliuk/nornir_pygnmi',
  download_url='https://github.com/akarneliuk/nornir_pygnmi/archive/v0.2.0.tar.gz',
  keywords=['gnmi', 'automation', 'grpc', 'network', 'pygnmi'],
  install_requires=[
          'nornir',
          'pygnmi'],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Intended Audience :: Telecommunications Industry',
    'Operating System :: OS Independent',
    'Topic :: System :: Networking',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10'
  ],
  python_requires=">=3.7",
    entry_points="""
    [nornir.plugins.connections]
    pygnmi=nornir_pygnmi.connection:PygnmiNornirConnectionPlugin
    """
)
