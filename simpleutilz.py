# pyutils.py
import datetime
import os
import json
import requests
import zipfile
import tarfile
from pathlib import Path
from urllib.parse import urlparse
import logging
import re
import configparser
from cryptography.fernet import Fernet
import PyPDF2


# File handling functions
def create_directory(directory_path):
    '''Create a directory if it does not exist.'''
    os.makedirs(directory_path, exist_ok=True)

def delete_file(file_path):
    '''Delete a file if it exists.'''
    if os.path.exists(file_path):
        os.remove(file_path)

# Data manipulation tools
def merge_dicts(*dicts):
    '''Merge multiple dictionaries into a single dictionary.'''
    merged_dict = {}
    for d in dicts:
        merged_dict.update(d)
    return merged_dict

# String utilities
def capitalize_first_letter(input_string):
    '''Capitalize the first letter of a given string.'''
    return input_string.capitalize()

def remove_whitespace(input_string):
    '''Remove leading and trailing whitespace from a string.'''
    return input_string.strip()

# Date and time utilities
def get_formatted_datetime(format_str="%Y-%m-%d %H:%M:%S"):
    '''Get the current date and time in a formatted string.'''
    return datetime.now().strftime(format_str)

# Logging module
def log_error(message):
    '''Log an error message to the console or a file (if configured).'''
    logging.error(message)

# Network utilities
def download_file(url, save_path):
    '''Download a file from a given URL and save it to the specified path.'''
    response = requests.get(url, stream=True)
    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)

def extract_zip(zip_file_path, extract_to):
    '''Extract files from a ZIP archive to the specified directory.'''
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def extract_tar(tar_file_path, extract_to):
    '''Extract files from a TAR archive to the specified directory.'''
    with tarfile.open(tar_file_path, 'r') as tar_ref:
        tar_ref.extractall(extract_to)

def get_domain_from_url(url):
    '''Extract the domain name from a given URL.'''
    parsed_url = urlparse(url)
    return parsed_url.netloc

# Other utilities
def generate_random_string(length=10):
    '''Generate a random string of a specified length.'''
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def is_prime(number):
    '''Check if a given number is a prime number.'''
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def load_json(file_path):
    '''Load JSON data from a file and return as a Python dictionary.'''
    with open(file_path, 'r') as json_file:
        return json.load(json_file)

def calculate_average(numbers):
    '''Calculate the average of a list of numbers.'''
    return sum(numbers) / len(numbers) if numbers else 0

def calculate_median(numbers):
    '''Calculate the median of a list of numbers.'''
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2

def flatten_list(nested_list):
    '''Flatten a nested list into a single-dimensional list.'''
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list

def remove_duplicates(input_list):
    '''Remove duplicates from a list while preserving the order.'''
    seen = set()
    unique_list = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    return unique_list

def is_valid_email(email):
    '''Check if a given string is a valid email address.'''
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email) is not None

def is_valid_url(url):
    '''Check if a given string is a valid URL.'''
    url_pattern = r'^(http|https|ftp)://.*$'
    return re.match(url_pattern, url) is not None

def is_valid_ipv4(ip):
    '''Check if a given string is a valid IPv4 address.'''
    ipv4_pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(ipv4_pattern, ip) is not None

def read_config_file(config_file_path):
    '''Read a configuration file (e.g., .ini, .yaml) and return as a dictionary.'''
    config = configparser.ConfigParser()
    config.read(config_file_path)
    config_dict = {}
    for section in config.sections():
        config_dict[section] = dict(config.items(section))
    return config_dict

def write_config_file(config_dict, file_path):
    '''Write a dictionary as a configuration file.'''
    config = configparser.ConfigParser()
    for section, section_data in config_dict.items():
        config[section] = section_data
    with open(file_path, 'w') as config_file:
        config.write(config_file)

def generate_encryption_key():
    '''Generate a new encryption key.'''
    return Fernet.generate_key()

def encrypt_string(text, key):
    '''Encrypt a string using a symmetric encryption algorithm.'''
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(text.encode())
    return encrypted_text

def decrypt_string(encrypted_text, key):
    '''Decrypt an encrypted string using the same key.'''
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(encrypted_text).decode()
    return decrypted_text

def convert_pdf_to_text(pdf_file_path):
    '''Convert a PDF file to plain text.'''
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        text = ''
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            text += page.extract_text()
        return text