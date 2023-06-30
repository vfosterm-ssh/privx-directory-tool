from setuptools import setup, find_packages

setup(
    name="privx-directory-tool",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Click", "rich>=12.6.0", "privx-api @ https://github.com/SSHcom/privx-sdk-for-python/archive/refs/tags/v29.0.0.zip"],
    entry_points={
        "console_scripts": [
            "privxdt = privxdt.main:cli",
        ],
    },
)
