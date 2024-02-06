# Clint

Simple **cli** program **int**egration testing using python and expect.

**NOTE** Some major changes are coming for this to make it more user friendly and more widely useful. This will include a name change and likely changing the setup to keep it as a single file lib/runner that can be added to a project without the need for installation. I may even change the programming language, since I now use babashka for most of my shell scripting and project building, though python is a good option due to it's general availability on most linux computers. I might also remove the use of expect and make it simpler overall.

I write a lot of command line programs that I like to test with something other than unit tests. For example, if I write a programming language and an interpreter it can be really nice to setup a spec for that language in tests before it is even implemented. Some of this can be done in unit tests, but these are often implementation dependent etc. This program is meant to make it easier for me to define tests in python (or even just plain data) as text to send to the program and text to expect back. It is also nice in situations like this to be able to have a failing test not stop the test suite from finishing, which often unit test frameworks do not do.

I wrote this project to handle some of the above for me. It is especially helpful when working on projects that do not have built in unit testing, like a simple C project or a project written in a language I made myself. However, this is only built with my own use cases in mind and if you happen across this you should find a more full featured and robust solution for your own testing needs.

# Commands
- test: `$ python3 setup.py pytest`
- build: `$ python3 setup.py bdist_wheel`
- install: `$ pip install dist/cli_test-0.1.0-py3-none-any.whl`
