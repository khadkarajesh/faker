from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="faker-np",
    version="0.0.3",
    description="Python package to generate the fake data in the context of Nepal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/khadkarajesh/faker/",
    author="Rajesh Khadka",
    author_email="rajesh.k.khadka@gmail.com",
    keywords="faker, fake data, Nepal, Nepali Names, Nepali Address",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7, <4",
    project_urls={  # Optional
        "Bug Reports": "https://github.com/khadkarajesh/faker/issues",
        "Source": "https://github.com/khadkarajesh/faker/",
    },
)
