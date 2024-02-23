from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MI',
    description='example of python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='<https://github.com/<Thebloodyracoon>/<mypackage>',
    author='<Thebloodyracoon>',
    author_email='<lablanamine@gmail.com>'
)