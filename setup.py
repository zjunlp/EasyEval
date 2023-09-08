from setuptools import setup, find_packages

setup(
    name='EasyEval',
    version='0.0.1',
    description='EasyEval',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=['openai', 'tqdm'],
)