# Tax Bracket API served on Modal

This repository contains a simple API deployed on modal for calculating tax brackets in different countries.

## Installation

1. Clone this repository: `git clone https://github.com/JSON-Lee-ai/net_income_calculator.git`
2. Navigate to the project directory: `cd net_income_calculator-api`
3. Install the modal dependencies: `pip install modal`
4. Set up modal: `python3 -m modal setup`

## Usage

The main functionality of this API is provided by the `Api` class in the `src` directory. Here are some examples of how to use it:

```bash
modal serve src/Api.py
```

```
% curl 'https://modal-labs--web-endpoint-get-net-income-dev.modal.run?gross-income=100000&country=US'
```

## Testing

This repository also includes a suite of unit tests. You can run these tests with the following command: python -m unittest ApiTest.py

## License
This project is licensed under the MIT License
