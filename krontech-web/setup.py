from setuptools import find_packages, setup

setup(
    name="krontech-web",
    version="0.13.2",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "krontech-core >= 3.0.0",
        "aiohttp >= 3.5.4",
        "alembic >= 0.9.2",
        "asyncpg >= 0.18.3, < 1.0.0",
        "cachetools >= 2.0.0",
        "psycopg2-binary >= 2.7.4",
        "injector >= 0.13.0",
        "pyjwt >= 1.5.0",
        "pyyaml >= 3.0",
        "pypika >= 0.28",
        "sqlalchemy >= 1.1.4",
        "yarl >= 1.1.0",
        "isodate >= 0.6.0, < 1.0.0",
        "redis >= 3.3.8, < 4.0.0",
        "addict >= 2.1.0, < 3.0.0",
        "jsonschema >= 3.0.0, < 4.0.0",
        "python-i18n >= 0.3, < 0.4",
    ],
)
