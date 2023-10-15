# Receipt Processor

**Table of Contents**
- [Introduction](#introduction)
- [Installation](#installation)
  - [Python Installation](#python-installation)
  - [POSTMAN Installation](#postman-installation)
  - [Required Libraries](#required-libraries)
- [Usage](#usage)
- [Execution](#execution)
- [Testing](#testing)

## Introduction

Receipt Processor is a Python project built with the Flask framework for processing receipts. This project allows you to parse and manage receipt data easily.

## Installation

Before you can run the Receipt Processor, you'll need to ensure you have Python installed and the required libraries available. Follow these steps to set up your environment.

### Python Installation

1. If you don't have Python installed, you can download it from the official Python website: [Python Downloads](https://www.python.org/downloads/).

2. Follow the installation instructions for your operating system.

### POSTMAN Installation

1. Go to the Postman download page for Windows at: https://www.postman.com/downloads/
2. Select the POSTMAN download option for your operation system.
3. A setup file will be downloaded to your computer. Locate the downloaded setup file and double-click it to run the installer.
4. Follow the on-screen instructions to complete the installation.
5. Once installed, you can launch Postman from your desktop or start menu.

### Required Libraries


The Receipt Processor project requires the following libraries, which can be installed using Python's package manager, pip:

  json - Used for working with JSON data.
  
  Flask - A micro web framework for building web applications.
  
  pytest - A testing framework for writing and running tests.
  
  hashlib - Used for various cryptographic operations, such as hashing.
  
  datetime - Provides classes for working with dates and times in Python.

```bash
pip install flask json pytest hashlib datetime
```

## Usage

1. Clone the repository to your local machine:
2. Open your terminal or command prompt.
3.Run the following command to clone the repository:

```bash
git clone https://github.com/belagaam/receipt_processor.git
```

4. Change your current directory to the newly cloned repository:

``` bash
cd receipt_processor
```

5. Run the Flask application. Start the Flask application by executing the following command:

``` bash
python receipt_processor.py
```

## Execution

Once the file has been executed the API can be checked by following the screenshot below:

Example JSON file:
```
{
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    }
  ],
  "total": "9.00"
}
```

Checking for POST request:
![WhatsApp Image 2023-10-15 at 11 48 03 PM](https://github.com/belagaam/receipt_processor/assets/47104198/d3ff5f54-9254-4e12-899e-949c0e63e91e)

Checking for GET request:
![WhatsApp Image 2023-10-15 at 11 47 12 PM](https://github.com/belagaam/receipt_processor/assets/47104198/7f7e8543-d840-4d47-b8f1-1b774d329806)

## Testing

The program can be tested for edge and corner cases by running the command
``` bash
pytest test_receipt_processor.py -v
```
