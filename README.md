#Python API Automation Framework

Hybrid Custom Framework to test the REST API's

#Tech Stack
1- Python 3.11
2- Request -  HTTP Requests
3- Pytest - Testing Framework
4- Reporting - Allure Report, Pytest HTML
5- Test Data -  CSV, Exscel, JSON
6- Parallel Execuation -  X distribute

#How to install packeges
 ``
 pip install requests pytest pytest-html faker allure-pytest jsonschema
``

#To freeze your packege version
``
pip freeze > requirments.txt
``
#To install the freeze version
``
pip install -r requirements.txt
``

#for parellel test case execution
``
pip install pytest-xdist
pytest -n auto test_parallel.py
``