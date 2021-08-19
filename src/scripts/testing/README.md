# Running tests with the test script

These scripts assume that postgres is up and running and Redis and Influx are reachable. 

### Running all tests

Use `./run_pytest_tests.sh` without any arguments to run all the tests in the tests folder

### Running specific tests

To run a single test, pass pytest arguments to `./run_pytest_tests.sh`, eg: `./run_pytests_tests /path/to/tests.py -k test_specific` to run only that test

See the `vars.sh` for variables.
