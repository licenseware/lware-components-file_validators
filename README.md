# File validators 

A package useful for validating files.

## Quickstart

In `requirements.txt` file add the following line:
```bash
#requirements.txt

git+https://git@github.com/licenseware/lware-components-file_validators.git

#other modules

```
You can install from requirements.txt with `pip3 install -r requirements.txt`

Alternatively you can install it with the command bellow:
```bash
pip3 install git+https://git@github.com/licenseware/lware-components-file_validators.git
```

## Usage
```py

from file_validators import GeneralValidator, validate_filename

v = GeneralValidator(
    input_object,           # required: file path, string or stream of bytes
    required_input_type,    # required: 'excel', 'csv', 'txt', 'string', 'stream'
    required_sheets   = [], # sheets names list that needs to be found in 'excel'
    required_columns  = [], # columns names list that needs to be found in 'excel', 'csv'
    text_contains_all = [], # text list that needs to be found in 'txt', 'string', 'stream'
    text_contains_any = [], # text list that needs to be found in 'txt', 'string', 'stream'
    min_rows_number   = 0   # minimum rows needed for 'excel', 'csv'
    header_starts_at  = 0   # row number where the header with columns starts (count starts from 0)
    buffer = 9000           # bytes to read from stream/file    
)

if v.validate():
    # other logic

#OR

res = v.validate(show_reason=True)

if res['status'] == 'success':
    return res['message']
elif res['status'] == 'fail':
    return res['message']


```


## Development

In case you need to add new functionality:
- `git clone` 
- `pipenv install`
- `pipenv shell`
- `pytest -v -s` or `pytest`
- test only one function: `pytest -v -s tests/test_file_name.py::test_function_name`


#### Useful resources

- [pandas docs](https://pandas.pydata.org/docs/reference/index.html)
- [cheatsheet pandas 1](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [cheatsheet pandas 2](https://www.dataquest.io/blog/pandas-cheat-sheet/)
- [performance optimizations](https://towardsdatascience.com/%EF%B8%8F-load-the-same-csv-file-10x-times-faster-and-with-10x-less-memory-%EF%B8%8F-e93b485086c7)
