## Ayesha OSINT Toolkit
This is my first OSINT toolkit project. It includes several tools for performing various OSINT (Open Source Intelligence) tasks such as username checking, email validation, and IP lookup. These scripts help gather information from publicly available data sources.



### Requirements
Python 3.x

requests library (for API calls)

### Installation
To install the required dependencies, run the following command in your terminal:
```
pip install -r requirements.txt
```

This will install all the necessary libraries required to run the scripts.

### Virtual Environment Setup

It is recommended to create a virtual environment before installing requirements:

```
python -m venv venv
source venv/bin/activate    # For Linux/Mac
venv\Scripts\activate       # For Windows
pip install -r requirements.txt
```

### Usage
Username Checker
Use this script to check if a username is available on various platforms.

#### Example usage:
```
python scripts/username_checker.py
```
### Email Finder
This script helps to find email addresses associated with a specific domain.

#### Example usage:
```

python scripts/email_finder.py
``` 

### IP Lookup
This script provides detailed information about an IP address, such as location, ISP, and more.

#### Example usage:
```
python scripts/ip_lookup.py
``` 

Each of the scripts is designed to perform a specific OSINT task, and you can run them individually based on your needs.

### Contribution
Feel free to fork this project, make changes, and send pull requests. Contributions are welcome!

```
License
This project is licensed under the MIT License.

MIT License

Copyright (c) 2023 SilentProgrammer-max

Permission is hereby granted, free of charge, to any person obtaining a copy  
of this software and associated documentation files (the "Software"), to deal  
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all  
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.
```


