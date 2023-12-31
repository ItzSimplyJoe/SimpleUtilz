# SimpleUtilz.py - Python Utility Library
`SimpleUtilz` is a versatile Python utility library that offers a wide range of helper functions, classes, and modules to expedite development tasks and simplify common operations. With `SimpleUtilz`, you can streamline your Python projects and enhance productivity through a collection of useful functionalities.

## Installation
You can install ``SimpleUtilz`` using pip:

`pip install simpleutilz`
## Functionality and Usage
### File Handling Functions
`create_directory(directory_path)`
Create a directory if it does not exist.


```py
from simpleutilz.simpleutilz import create_directory

directory_path = '/path/to/directory'
create_directory(directory_path)
```
`delete_file(file_path)`
Delete a file if it exists.

```py
from simpleutilz.simpleutilz import delete_file

file_path = '/path/to/file.txt'
delete_file(file_path)
```
### Data Manipulation Tools
merge_dicts(*dicts)
Merge multiple dictionaries into a single dictionary.


```py
from simpleutilz.simpleutilz import merge_dicts

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```
### String Utilities
`capitalize_first_letter(input_string)`
Capitalize the first letter of a given string.

```py
from simpleutilz.simpleutilz import capitalize_first_letter

input_string = 'hello world'
capitalized_string = capitalize_first_letter(input_string)
print(capitalized_string)  # Output: 'Hello world'
```
`remove_whitespace(input_string)`
Remove leading and trailing whitespace from a string.

```py
from simpleutilz.simpleutilz import remove_whitespace

input_string = '   hello world   '
cleaned_string = remove_whitespace(input_string)
print(cleaned_string)  # Output: 'hello world'
```
### Date and Time Utilities
`get_formatted_datetime(format_str="%Y-%m-%d %H:%M:%S")`
Get the current date and time in a formatted string.

```py
from simpleutilz.simpleutilz import get_formatted_datetime

formatted_time = get_formatted_datetime("%Y-%m-%d")
print(formatted_time)  # Output: '2023-07-20'
```
### Logging Module
`log_error(message)`
Log an error message to the console or a file (if configured).

```py
import logging
from simpleutilz.simpleutilz import log_error

logging.basicConfig(filename='error.log', level=logging.ERROR)
try:
    # Some code that may raise an exception
    raise ValueError("Something went wrong!")
except Exception as e:
    log_error(str(e))
```
### Network Utilities
`download_file(url, save_path)`
Download a file from a given URL and save it to the specified path.

```py
from simpleutilz.simpleutilz import download_file

file_url = 'https://example.com/some_file.txt'
save_path = '/path/to/save/file.txt'
download_file(file_url, save_path)
```
`extract_zip(zip_file_path, extract_to)`
Extract files from a ZIP archive to the specified directory.

```py
from simpleutilz.simpleutilz import extract_zip

zip_file_path = '/path/to/archive.zip'
extract_to = '/path/to/extract'
extract_zip(zip_file_path, extract_to)
```
`extract_tar(tar_file_path, extract_to)`
Extract files from a TAR archive to the specified directory.

```py
from simpleutilz.simpleutilz import extract_tar

tar_file_path = '/path/to/archive.tar.gz'
extract_to = '/path/to/extract'
extract_tar(tar_file_path, extract_to)
```
`get_domain_from_url(url)`
Extract the domain name from a given URL.

```py
from simpleutilz.simpleutilz import get_domain_from_url

url = 'https://www.example.com/some/page.html'
domain = get_domain_from_url(url)
print(domain)  # Output: 'www.example.com'
```
## Other Utilities
`generate_random_string(length=10)`
Generate a random string of a specified length.

```py
from simpleutilz.simpleutilz import generate_random_string

random_str = generate_random_string(8)
print(random_str)  # Output: 'JwB45XzQ'
```
`is_prime(number)`
Check if a given number is a prime number.

```py
from simpleutilz.simpleutilz import is_prime

number = 17
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
```
`load_json(file_path)`
Load JSON data from a file and return it as a Python dictionary.

```py
from simpleutilz.simpleutilz import load_json

file_path = '/path/to/data.json'
data = load_json(file_path)
print(data)  # Output: {'name': 'John Doe', 'age': 30, 'email': 'john@example.com'}
```
`calculate_average(numbers)`
Calculate the average of a list of numbers.
```py
from simpleutilz.simpleutilz import calculate_average

numbers = [12, 34, 56, 78, 90]
average = calculate_average(numbers)
print(average)  # Output: 54.
```
`calculate_median(numbers)`
Calculate the median of a list of numbers.
```py
from simpleutilz.simpleutilz import calculate_median

numbers = [12, 34, 56, 78, 90]
median = calculate_median(numbers)
print(median)  # Output: 56
```
`flatten_list(nested_list)`
Flatten a nested list into a single-dimensional list.

```
from simpleutilz.simpleutilz import flatten_list

nested_list = [[1, 2, 3], [4, [5, 6]], [7], 8]
flattened_list = flatten_list(nested_list)
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
```
`remove_duplicates(input_list)`
Remove duplicates from a list while preserving the order.
```py
from simpleutilz.simpleutilz import remove_duplicates

input_list = [1, 2, 2, 3, 4, 3, 5]
unique_list = remove_duplicates(input_list)
print(unique_list)  # Output: [1, 2, 3, 4, 5]
```
`is_valid_email(email)`
Check if a given string is a valid email address.

```py
from simpleutilz.simpleutilz import is_valid_email

email = 'john@example.com'
if is_valid_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")
```
`is_valid_url(url)`
Check if a given string is a valid URL.

```py
from simpleutilz.simpleutilz import is_valid_url

url = 'https://www.example.com'
if is_valid_url(url):
    print(f"{url} is a valid URL.")
else:
    print(f"{url} is not a valid URL.")
```
`is_valid_ipv4(ip)`
Check if a given string is a valid IPv4 address.

```py
from simpleutilz.simpleutilz import is_valid_ipv4

ip = '192.168.1.1'
if is_valid_ipv4(ip):
    print(f"{ip} is a valid IPv4 address.")
else:
    print(f"{ip} is not a valid IPv4 address.")
```
`read_config_file(config_file_path)`
Read a configuration file (e.g., .ini, .yaml) and return it as a dictionary.

```py
from simpleutilz.simpleutilz import read_config_file

config_file_path = '/path/to/config.ini'
config_data = read_config_file(config_file_path)
print(config_data)
```
`write_config_file(config_dict, file_path)`
Write a dictionary as a configuration file.

```py
from simpleutilz.simpleutilz import write_config_file

config_dict = {'Section1': {'key1': 'value1', 'key2': 'value2'}, 'Section2': {'key3': 'value3'}}
file_path = '/path/to/config.ini'
write_config_file(config_dict, file_path)
```
`generate_encryption_key()`
Generate a new encryption key.
```py
from simpleutilz.simpleutilz import generate_encryption_key

encryption_key = generate_encryption_key()
print(encryption_key)
```
`encrypt_string(text, key)`
Encrypt a string using a symmetric encryption algorithm.
```py
from simpleutilz.simpleutilz import encrypt_string

text = 'This is a secret message.'
key = b'some_random_key'
encrypted_text = encrypt_string(text, key)
print(encrypted_text)
```
`decrypt_string(encrypted_text, key)`
Decrypt an encrypted string using the same key.

```py
from simpleutilz.simpleutilz import decrypt_string

encrypted_text = b'encrypted_data_here'
key = b'some_random_key'
decrypted_text = decrypt_string(encrypted_text, key)
print(decrypted_text)
```
`convert_pdf_to_text(pdf_file_path)`
Convert a PDF file to plain text.

```py
from simpleutilz.simpleutilz import convert_pdf_to_text

pdf_file_path = '/path/to/sample.pdf'
pdf_text = convert_pdf_to_text(pdf_file_path)
print(pdf_text)
```

`convert_value_to_denary(hexValue, "hex")`
Convert Hex to Denary
```py
from simpleutilz.simpleColours import convert_value_to_denary

hexValue = '#ffffff'
denary = convert_value_to_denary(hexValue, "hex")
print(denary)
```

`convert_value_to_denary(rgbValue, "rgb")`
Convert RGB to Denary
```py
from simpleutilz.simpleColours import convert_value_to_denary

rgbValue = (255, 255, 255)
denary = convert_value_to_denary(rgbValue, "rgb")
print(denary)
```

`convert_value_to_denary(rgbaValue, "rgba")`
Convert RGBA to Denary
```py
from simpleutilz.simpleColours import convert_value_to_denary

rgbaValue = (255, 255, 255, 1)
denary = convert_value_to_denary(rgbaValue, "rgba")
print(denary)
```

`convert_value_to_denary(binaryValue, "binary")`
Convert Binary to Denary
```py
from simpleutilz.simpleColours import convert_value_to_denary

binaryValue = '11111111'
denary = convert_value_to_denary(binaryValue, "binary")
print(denary)
```

`colour = RGB_to_colour(rgbValue)`
Convert RGB code to Colour in English
```py
from simpleutilz.simpleColours import RGB_to_colour

rgbValue = (255, 255, 255)
colour = RGB_to_colour(rgbValue)
print(colour)
```

`hex_to_colour(hexValue)`
Convert Hex code to Colour in English
```py
from simpleutilz.simpleColours import hex_to_colour

hexValue = '#ffffff'
colour = hex_to_colour(hexValue)
print(colour)
```

`RGBA_to_colour(rgbaValue)`
Convert RGBA code to Colour in English
```py
from simpleutilz.simpleColours import RGBA_to_colour

rgbaValue = (255, 255, 255, 1)
colour = RGBA_to_colour(rgbaValue)
print(colour)
```

`binary_to_colour(binaryValue)`
Convert Binary code to Colour in English
```py
from simpleutilz.simpleColours import binary_to_colour

binaryValue = '11111111'
colour = binary_to_colour(binaryValue)
print(colour)
```

## Contributing
Contributions to `SimpleUtilz` are welcome! If you find any bugs, have new ideas, or want to improve the existing functionality, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

The `SimpleUtilz` library offers an extensive array of functions to simplify tasks and boost productivity in Python projects. The README.md provides detailed explanations and examples for each function, enabling users to grasp the functionalities swiftly and incorporate them seamlessly into their projects. Should you encounter any issues or have suggestions for improvements, do not hesitate to contribute or reach out to me!
