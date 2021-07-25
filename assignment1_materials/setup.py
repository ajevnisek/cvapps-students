from setuptools import setup, find_packages


version = '0.0.1'


setup(
    name='cvapps_sol_checker',
    version=version,
    description='CVApps course checker',
    long_description=open('README.md').read(),
    license='MIT',
    author='Amir Jevnisek',
    author_email='ajevnisek@gmail.com',
    url='https://github.com/ajevnisek/cvapps-students.git',
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
    ],
    packages=find_packages('src', exclude=["tests*"]),
    package_dir={'': 'src'},
)
