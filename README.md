# file_parse_test
<br>
<h3>Instructions</h3>
- Download 'file_parse_test' repo<br>
- go to 'file_parse_test/test_files/' folder<br>
- install requirements/libraries using this command: pip install -r requirements.txt<br>
- run the following command to run ALL tests: ./run_tests.sh full_test<br>
- run the following command to run SMOKE Tests: ./run_tests.sh smoke_test

<br><br>
<h4>NOTES:</h4>
- Using Unittest framework<br>
- Some assumptions are made and are written inside the test file. On a real project, these assumptions should be made clear with PMs or Project Leads<br>
- Ran these tests in a virtual environment using Python 2.7 and they passed. Let me know if you encounter some trouble.<br>
- log.py and setup_teardown.py were added for future enhancements.<br>
- 'test_suites' folder contains the test suites you can run. very useful when you have hundreds/thousands of tests and for CI. running SMOKE tests when time contrained and FULL tests otherwise.<br>
- 'files' folder contains test files used for test cases<br>
- 'requirements.txt' contains libraries used in this exercise<br>
<br>

<h4>Console Output</h4>
*** Happy path test *** ../files/testFile.txt
<br>Lines in File: ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcde', 'edcba']
<br>Largest words: ['abcde', 'abcde', 'edcba']
<br>Reversed words: ['edcba', 'edcba', 'abcde']
<br>*** Empty file test *** ../files/testEmptyFile.txt
<br>Lines in File: []
<br>Largest words: []
<br>Reversed words: []
<br>*** Sentences in File test *** ../files/testSentencesFile.txt
<br>Lines in File: ['TestRail helps you manage and track your software testing efforts and organize your QA department.', 'Its intuitive web-based user interface makes it easy to create test cases, manage test runs and coordinate your entire testing process.', '', 'Easily track and follow the status of individual tests, milestones and projects with dashboards and activity reports.', 'Get real-time insights into your testing progress and boost productivity with personalized todo lists, filters and email notifications.', 'Efficient test management, get started today!']
<br>Largest words: ['notifications.']
<br>Reversed words: ['.snoitacifiton']
<br>*** File Does Not Exist test *** ../files/testFileDoesNotExist.txt
<br>File '../files/testFileDoesNotExist.txt' not exist
<br>*** Invalid file format test *** ../files/testImageFile.png
<br>File format is invalid. Only accepts .dat and .txt<br>