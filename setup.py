from setuptools import setup, find_packages

with open('README.md') as file:
    README = file.read()

setup(
    name='test-pypi-workflow-mlreflect',
    version='0.0.1',
    packages=find_packages(),
    long_description=README,
    long_description_content_type='text/markdown',
    author='Alessandro Greco',
    author_email='alessandro.greco@gmx.net',
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.6'
)
