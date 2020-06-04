from setuptools import find_packages, setup

setup(
    name='krontech-core',
    version='3.1.0',
    packages=find_packages('src'),
    namespace_packages=['krontech'],
    package_dir={'': 'src'},
    install_requires=[
        'PyYAML >= 3.11',
        'aiozmq >= 0.5.3',
        'injector >= 0.13.0, < 0.16.0',
        'msgpack < 1.0.0',
        'ntplib >= 0.3.2',
        'pyzmq >= 14.4.1',
        'aiohttp >= 3.0.0, < 4.0.0',
        'aiohttp-jinja2 >= 0.17.0, < 1.0.0',
        'aiohttp-cors >= 0.7.0, < 1.0.0',
        'pyformance >= 0.3.2',
        'Jinja2 >= 2.8',
        'numpy >= 1.9.1',
        'msgpack_numpy >= 0.4.2',
        'async-timeout >= 2.0.0',
        'cachetools >= 2.0.0',
        'sqlalchemy >= 1.0',
        'alembic >= 0.9.2',
        'attrs >= 17.4.0',
    ],
)
