from setuptools import setup, find_packages

setup(
    name='demodata',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'barnum',
        'future',
        'names',
        'python-dateutil',
        'six',
        'Click',
    ],
    entry_points='''
        [console_scripts]
        demodata=demodata.scripts.entry:cli
    ''',
)
