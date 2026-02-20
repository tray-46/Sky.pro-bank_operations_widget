# Sky.pro-bank_operations_widget

<details>
    <summary>Table of Content</summary>
    <ol>
        <li>
            <a href="#about-the-project">About the project</a>
        </li>
        <li>
          <a href="#getting-started">Getting started</a>
        </li>        
        <li>
          <a href="#usage">Usage</a>
        </li>
        <li>
          <a href="#testing">Testing</a>
        </li>
    </ol>
</details>

## About the project
A training project - implementing the backend portion of a banking widget displaying a list of the most recent successfully completed transactions

### Build with
* [![Python](https://img.shields.io/badge/Python%20IDLE-3776AB?logo=python&logoColor=fff)](https://python.org/)
* [![PyCharm](https://img.shields.io/badge/PyCharm-000?logo=pycharm&logoColor=fff)](https://www.jetbrains.com/pycharm/)

## Getting started
To clone the repository use the following links:

* with HTTPS:
```
    https://github.com/tray-46/Sky.pro-bank_operations_widget.git
```

* with SSH:  
```
    git@github.com:tray-46/Sky.pro-bank_operations_widget.git
```

## Usage
The following functions are implemented in the project:
1. function to get masked bank card number:  
`get_mask_card_number`

2. function to get masked bank account number:  
`get_mask_account`

3. function to get masked bank account or card number:  
`mask_account_card`

4. function to get formatted date string:  
`get_date`

5. function for filtering operations list by targeted state:  
`filter_by_state`

6. function for sorting operations list by date:  
`sort_by_date`

7. function to get iterator with transactions filtered by currency:  
`filter_by_currency`

8. generator function to get transactions descriptions:  
`transaction_descriptions`

9. generator function for generating card numbers within a given range:  
`card_number_generator`


### Usage examples
Examples of using the functions can be found in the [documentation](docs/usage_examples.md).

## Testing
Project was tested with pytest framework and got 100% code coverage.  
[Coverage report](htmlcov/index.html)   
