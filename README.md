# Easy Connector with Odoo ERP!
This is a library that allow an easy and friendly connection with an Odoo ERP instance on Pyhton 3.x

## Installation using PIP command
- Use the command
```shell
$ pip install odoo_connector_2
```

## How to use connect
```python
from odoo.connectors import OdooConnector
odoo = OdooConnector(endpoint='your-odoo-endpoint', dbname='your-odoo-dbname', username='your-odoo-user', password='your-odoo-password')
uid = odoo.connect()
```
### Hot to add, edit and delete ( using the method write() )
```python
from odoo.connectors import OdooConnector
odoo = OdooConnector(endpoint='your-odoo-endpoint', dbname='your-odoo-dbname', username='your-odoo-user', password='your-odoo-password')
uid = odoo.connect()
# create a new partner
data = [{'name': 'Test User', 'email': 'test@domain.com'}]
result = odoo.write(uid=uid, model='res.partner', action='create', data=data)

# edit partner
id = 1 # change the value for the any do you want
data = [[id], {'name': 'Test User', 'email': 'test@domain.com'}]
result = odoo.write(uid=uid, model='res.partner', action='write', data=data)

# delete partner
id = 1 # change the value for the any do you want
data = [id]
result = odoo.write(uid=uid, model='res.partner', action='unlink', data=data)

# create a new user
data = [{'login': 'test@domain.com', 'name': 'Test User', 'password': '123456'}]
result = odoo.write(uid=uid, model='res.users', action='signup', data=data)
```

### Hot to search, search_read and read ( using the method search() )
```python
from odoo.connectors import OdooConnector
odoo = OdooConnector(endpoint='your-odoo-endpoint', dbname='your-odoo-dbname', username='your-odoo-user', password='your-odoo-password')
uid = odoo.connect()

query = [[['is_company', '=', True], ['customer', '=', True]]]
fields = ['name', 'email', 'country_id']

# using the search method
result = odoo.search(uid=uid, model='res.partner', action='search', queries=query, parameters=None)

 # using the search with pagination
parameters = {'offset': 5, 'limit': 10}
result = odoo.search(uid=uid, model='res.partner', action='search', queries=query, parameters=parameters)

# using the search_count
odoo.search(uid=uid, model='res.partner', action='search_count', queries=query)

# using the read method
ids = odoo.search(uid=uid, model='res.partner', action='search', queries=query, parameters={'limit': 1})
if len(ids) > 0:
    result = self.odoo.search(
        uid=uid, model='res.partner', action='read', queries=ids, parameters={'fields': fields}  formatted=True)

# The "formatted" attribute allow format the result in a JSON object, this is a boolean attribute by default is False

# using the search_read method with parameters.
result = odoo.search(
            uid=uid, model='res.partner', action='search_read', queries=query, parameters={'fields': fields, 'limit': 2}, formatted=True)
```

The search and write methods were tested with all methods allowed on the External API Documentation from Odoo website
and the write() and search() methods can work with any methods from any models existing on Odoo instance

### To test any methods using unittest

- Download or clone this repository
- Edit the attributes from the DummieData class (find this class on tests/unittests.py)
- run the follow command on the root directory.
```shell
$ python -m unittest -v tests/unittest.py
```