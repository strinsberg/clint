from setuptools import find_packages, setup

setup(
    name="cli_test",
    packages=find_packages(include=["cli_test"]),
    version="0.1.0",
    description="Simple testing for cli programs built on expect",
    author="Strinsberg",
    license="MIT",
    install_requires=["pexpect==4.8.0"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==7.4.1"],
    test_suite="tests",
)
