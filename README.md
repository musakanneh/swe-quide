# Test Driven Development (TDD)

If it's not tested it doesn't work!

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/246/giphy-4.gif)

## Overview

Test Driven Development is a process where the developer takes responsibility for writing quality code.
TDD recommends writing tests that would check the functionality of your code prior to your writing the actual code.

## Levels of testing

- Unit Testing: tests at the function level

  - Tests individual functions in a program
  - Groups of unit test can be combined into test suites
  - Executes in development environment instead of production environment
  - Test is implemented in an automated fashion

### Steps in performing a unittest

  - Setup step: testing the test strings
  - Action step: calls the production code to perform the action that is on the test
  - Assertion step: where the test validates the result of the action

- Component Testing: Testing at the library and complete binary level
- System Testing: tests the external interfaces of a system which is a collection of sub-systems
- Performance Testing: testing done at the sub-system and system levels to verify timing and resource usages are acceptable
