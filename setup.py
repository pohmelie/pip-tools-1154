from pathlib import Path

from setuptools import find_packages, setup

PACKAGE_ROOT = Path(__file__).parent


def read_requirements(name: str):
    p = PACKAGE_ROOT.joinpath(name)
    reqs = []
    for line in p.read_text().splitlines():
        if not line or line.startswith("#"):
            continue
        req = line
        req = req.split("# ")[0].strip()
        if req.startswith("file:"):
            relative = Path(req[len("file:"):])
            virtual = Path("localhost", PACKAGE_ROOT.relative_to("/"), relative)
            req = f"{relative.name} @ file://{virtual}"
        reqs.append(req)
    return reqs


setup(
    name="monitoring-server",
    version="1.0.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=read_requirements("requirements/production.txt"),
)
