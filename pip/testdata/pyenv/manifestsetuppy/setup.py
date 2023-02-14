from setuptools import setup, find_packages

setup(
    name='test_project'
    version='1.0'
    author='xyz'
    email='abc@xyz.com'
    description='Test project'
    package=find_packages(),
    install_requires = [
        'numpy>=1.16.0',
        'matplotlib>=3.0.0',
        'pandas>=0.24.0'
    ],
    python_requires>='3.6'
)