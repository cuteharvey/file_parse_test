# file_parse_test
<br>
<h3>Instructions</h3>
- Download 'file_parse_test' repo<br>
- main test file is 'file_parse_test/test_files/file_tests/test_parse_file.py'<br>
- to run test, go to 'file_parse_test/test_files/file_test' folder<br>
- run the following command: python ./test_parse_file.py

<br><br>
<h4>NOTES:</h4>
- Not using any runners or test framework here. Just a simple test structure to run the tests.<br>
- Some assumptions are made and are written inside the test file. On a real project, these assumptions should be made clear with PMs or Project Leads<br>
<br><br>

<h4>Console Output</h4>
*** Happy path test ***<br>
Lines in File: ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcde', 'edcba']<br>
Largest words: ['abcde', 'abcde', 'edcba']<br>
Reversed words: ['edcba', 'edcba', 'abcde']<br>
*** Empty file test ***<br>
Lines in File: []<br>
Largest words: []<br>
Reversed words: []<br>
*** Sentences in File test ***<br>
Lines in File: ['TestRail helps you manage and track your software testing efforts and organize your QA department.', 'Its intuitive web-based user interface makes it easy to create test cases, manage test runs and coordinate your entire testing process.', '', 'Easily track and follow the status of individual tests, milestones and projects with dashboards and activity reports.', 'Get real-time insights into your testing progress and boost productivity with personalized todo lists, filters and email notifications.', 'Efficient test management, get started today!']
<br>Largest words: ['notifications.']<br>
Reversed words: ['.snoitacifiton']<br>
*** File Does Not Exist test ***<br>
File '../files/testFileDoesNotExist.txt' not exist<br>
*** Invalid file format test ***<br>
File format is invalid. Only accepts .dat and .txt<br>