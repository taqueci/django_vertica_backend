from distutils.core import setup

setup(
    name='django_vertica_backend',
    version='0.0.0',
    packages=['vertica'],
    url='https://github.com/emushell/django_vertica_backend',
    license='MIT license',
    author='emushell',
    author_email='emushell@example.com',
    description='Vertica backend for Django 3.0',
    install_requires=['vertica-python'],
)
