import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="today",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="基于爬虫的历法查询工具",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages("today"),
    entry_points={'console_scripts': [
            'td = today.main:main',
        ]},
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
)
