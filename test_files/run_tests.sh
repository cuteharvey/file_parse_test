#!/bin/bash
#README: example command: ./run_tests.sh full_test (optional)
#param = full_test (default), smoke_test (this is the test suite filename)

if [ -z $1 ]
then
    suite="full_test"
    export SUITE_TYPE="full_test"
else
    suite=$1
    export SUITE_TYPE=$1
fi

timestamp=$(date '+%Y%m%d%H%M%S')
tests=`cat test_suites/"$suite".txt`
echo $tests

cd "file_tests"

for f in $tests; do python -m xmlrunner $f; done
echo
echo "Finished running tests..."

