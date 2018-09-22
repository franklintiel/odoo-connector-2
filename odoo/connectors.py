from .protocols import OdooProtocol
from xmlrpc import client
from xmlrpc.client import Error
import json


class OdooConnector(OdooProtocol):
    username = None
    password = None
    endpoint = None
    link_type = None
    dbname = None
    client = client
    
    def __init__(self, endpoint, dbname, username, password):
        self.endpoint = endpoint
        self.dbname = dbname
        self.username = username
        self.password = password
    
    def link(self, link_type='common'):
        connection = None
        url = '{0}/xmlrpc/2/{1}'.format(self.endpoint, link_type)
        try:
            connection = client.ServerProxy(url, allow_none=1, encoding='utf8')
        except Error as error:
            raise error
        except OSError as error:
            raise error
        except ConnectionRefusedError as error:
            raise error
        return connection

    def connect(self, dbname=None, username=None, password=None):
        connection = self.link()
        uid = None
        _username = username if username else self.username
        _password = password if password else self.password
        _dbname = dbname if dbname else self.dbname
        if _username and _password and _dbname:
            try:
                uid = connection.authenticate(_dbname, _username, _password, {})
            except Error as error:
                raise error
            except OSError as error:
                raise error
            except ConnectionRefusedError as error:
                raise error
        return uid

    def write(self, uid, model, action, data, password=None):
        result = None
        _password = password if password else self.password
        if model and action and uid:
            connection = self.link(link_type='object')
            try:
                result = connection.execute_kw(
                    self.dbname, uid, _password, model, action, data)
            except Error as error:
                raise error
            except OSError as error:
                raise error
            except ConnectionRefusedError as error:
                raise error
        return result

    def search(self, uid, model, action, password=None, queries=None, parameters=None, formatted=False):
        result = None
        _password = password if password else self.password
        if model and action and uid:
            connection = self.link(link_type='object')
            try:
                output = connection.execute_kw(
                    self.dbname, uid, _password, model, action, queries, parameters)
                if formatted:
                    result = json.dumps(self.output_formatter(output))
                else:
                    result = output
            except Error as error:
                raise error
            except OSError as error:
                raise error
            except ConnectionRefusedError as error:
                raise error
        return result

    def output_formatter(self, result=[]):
        output_formatted = []
        for item in result:
            obj = {}
            for key, value in item.items():
                value_tmp = value
                if 'list' not in value.__class__.__name__:
                    value_tmp = None if not value else value
                if value_tmp:
                    if 'list' in value_tmp.__class__.__name__:
                        if len(value_tmp) == 2:
                            if 'str' in value_tmp[1].__class__.__name__:
                                obj[key] = {
                                    'id': int(value_tmp[0]),
                                    'value': str(value_tmp[1])}
                            else:
                                obj[key] = value_tmp
                        else:
                            obj[key] = value_tmp
                    else:
                        obj[key] = value_tmp
            output_formatted.append(obj)
        return output_formatted
