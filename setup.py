from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pip==19.0.3",
"wheel==0.33.1",
"jsonrpcserver>=5.0.0",
"xlrd>=2.0.1"
] # 这里填依赖包信息

setup(
    name="hgcTestPkg",
    version="0.0.37",
    author="ghc",
    author_email="g51301727@gmail.com",
    description="to test how to release a pkg",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/LimerenceGL/ghcTestPkg.git",
    packages=find_packages(),
    # Single module也可以：
    # py_modules=['timedd']
    install_requires=requirements,
    classifiers=[
	"Programming Language :: Python :: 3.10",
	"License :: OSI Approved :: MIT License",
    ],
)