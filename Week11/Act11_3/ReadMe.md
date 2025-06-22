### 1. Describe what each test method is checking.
- The test_upper checks whether the upper() function correctly converts the string 'foo' to uppercase, expecting the result to be 'FOO'. 
- The test_isupper method evaluates the isupper() function by first confirming that 'FOO' (all uppercase) returns True, and then confirming that 'Foo' (not all uppercase) returns False. 
- The test_split method tests if splitting the string 'hello world' produces the list ['hello', 'world'], and also checks that attempting to use a non-string separator (specifically, the integer 2) in the split() function raises a TypeError.


### 2. Run the code and interpret the results.
- The unittest framework automatically detects and runs test methods in the class. If all assertion is correct the output will show 'OK', inidicating it is succesful. If any test fails there will be an 'FAILED' and explains what fails and why it fails. 



### 3. Modify the code to add a new test case that checks if '123'.isdigit() returns True.

def test_digit(self):
        self.assertTrue('123'.isdigit())

it shows OK


### 4. What happens if one of the assertions fails? Try changing one expected value and observe the result.
- If one fails, FAILED will show in ouput. it will also show how many failed, why and what failed. 