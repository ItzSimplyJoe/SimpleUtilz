from setuptools import setup, find_packages

# Package metadata
NAME = 'simpleutilz'
VERSION = '1.0.1'
DESCRIPTION = 'A versatile Python utility library that offers a wide range of helper functions, classes, and modules to expedite development tasks and simplify common operations'
URL = 'https://github.com/ItzSimplyJoe/SimpleUtilz'
AUTHOR = 'ItzSimplyJoe'
EMAIL = 'joebostock30@gmail.com'

# Package dependencies (if any)
INSTALL_REQUIRES = [
    # List any dependencies your package requires here
    'requests',
]

# Package classifiers (see https://pypi.org/classifiers/)
CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Operating System :: OS Independent',
]

# Package entry points (if any)
# entry_points = {
#     'console_scripts': [
#         'your_command=your_package.module:main_function',
#     ],
# }

# Read the long description from README.md
with open('README.md', 'r', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    packages=find_packages(),  # Automatically discover and include all packages in the project
    install_requires=INSTALL_REQUIRES,
    classifiers=CLASSIFIERS,
    # entry_points=entry_points,  # Uncomment this if you have any entry points
)
