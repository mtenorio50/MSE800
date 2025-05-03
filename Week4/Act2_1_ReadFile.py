with open('D:\\YooBee\\HelloWorld\\MSE800\\Week4\\sample_text.txt', 'r') as file:
    content = file.read()

underscore_count = content.count('__')
print(content)
print(f"Number of underscores in the text file: {underscore_count}")
