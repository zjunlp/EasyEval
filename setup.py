from setuptools import setup, find_packages
from setuptools.command.install import install

REQUIRES = """
openai
tqdm
"""


def get_install_requires():
    reqs = [req for req in REQUIRES.split("\n") if len(req) > 0]
    return reqs


with open("README.md") as f:
    readme = f.read()


def do_setup():
    setup(
        name="easyeval",
        version='0.0.1',
        description="EasyEval",
        url="https://github.com/zjunlp/EasyEval/tree/main",
        author='Yida Xue',
        long_description=readme,
        long_description_content_type="text/markdown",
        install_requires=get_install_requires(),
        python_requires=">=3.7.0",
        packages=find_packages(),
        keywords=["AI", "NLP", "instruction", "language model"],
        classifiers=[
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
        ]
    )


if __name__ == "__main__":
    do_setup()
