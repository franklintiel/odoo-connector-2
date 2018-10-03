import unittest
from odoo_connector.connectors import OdooConnector

class DummieData(object):
    """
    Dummie data used to test all unit tests.
    :var ODOO_USERNAME: string  (The odoo user to connect with Odoo Instance)
    :var ODOO_PASSWORD: string (The odoo user password to connect with Odoo instance)
    :var ODOO_ENDPOINT: string (The endpoint to connect with Odoo instance by default is required and this should be started with http:// protocol)
    :var ODOO_DBNAME: string (The database name to connect with Odoo Instance)
    :var PERMISSIONS: list (List with only a permission to check if the user has permissions on the model selected by example to test: ['read'].)
        :var QUERY_FILTER: list (List the query filters defined to apply on the search, search_read, search_count, read, name_get methods.)
    :var PARTNER_FIELDS: list (List to fields required to get info related from the model selected .)
    :var FIELD_ATTRIBUTES: list (List from strings with the attribute names required from fields from the model selected on the fields_get method.)
    :var NEW_PARTNER_DATA: list (List from dictiony with the fields and values required to create a new record from the model selected on the create method.)
    :var CAN_CREATE: boolean (By default is False, change to True if you want test the create method)
    :var ID_TO_UPDATE_OR_SELECT: int (By default is 0, add ID existing on the Odoo instance related with the model used to test the updated method.)
    :var UPDATE_PARTNER_DATA: dictionary (Dictionary with the model info required to update using the update method.)
    :var CAN_UPDATE: boolean (By default is False, change to True and add an ID from Odoo Model related on ID_TO_UPDATE to test the update method.)
    :var ID_TO_DELETE: boolean (By default is 0, change the ID from record related with the model selected on the unlink method.)
    :var CAN_DELETE: boolean (By default is False, change to True if you want to remove the record selected using the ID_TO_DELETE as reference.)
    :var NEW_USER_DATA: list (List with info to create a new user using the signup method, before to test this, you need sure that general settings is adjusted to allow new external users.)
    :var CAN_SIGNUP: boolean (By default is False, change to True if you want test the signup method.)
    :var ID_TO_SELECT: int (By default is 0, add Id existing on the Odoo instance related with the model used)
    """
    ODOO_USERNAME = ''
    ODOO_PASSWORD = ''
    ODOO_ENDPOINT = ''
    ODOO_DBNAME = ''
    PERMISSIONS = []
    QUERY_FILTER = []
    PARTNER_FIELDS = []
    FIELD_ATTRIBUTES = []
    NEW_PARTNER_DATA = []
    CAN_CREATE = False
    ID_TO_UPDATE = 0
    UPDATE_PARTNER_DATA = {}
    CAN_UPDATE = False
    ID_TO_DELETE = 0
    CAN_DELETE = False
    NEW_USER_DATA = []
    CAN_SIGNUP = False
    ID_TO_SELECT = 0


class TestOdooInstance(unittest.TestCase):

    def setUp(self):
        """
        Creating Odoo instance from Odoo connector
        :return: None
        """
        self.odoo = OdooConnector(
            username=DummieData.ODOO_USERNAME, password=DummieData.ODOO_PASSWORD,
            dbname=DummieData.ODOO_DBNAME, endpoint=DummieData.ODOO_ENDPOINT)

    def test_odoo_instance(self):
        """
        Test to check the Odoo instance using the OdooConnector class.
        :return: None
        """
        self.assertIsNotNone(self.odoo)
        self.assertIsNotNone(self.odoo.username)
        self.assertIsNotNone(self.odoo.password)
        self.assertIsNotNone(self.odoo.endpoint)

    def test_odoo_link_built(self):
        """
        Test to check the link connection to Odoo instance through OdooConnector class.
        :return: None
        """
        result = self.odoo.link()
        self.assertTrue(hasattr(result, 'version'), False)
        self.assertIsNotNone(result.version())

    def test_odoo_admin_user_login(self):
        """
        Test to check the login from the odoo admin user using the OdooConnector class.
        :return: None
        """
        uid = self.odoo.connect()
        self.assertGreater(uid, 0)

    def test_calling_create_method(self):
        """
        Test the create method using the OdooConnector class.
        :return: None
        """
        if DummieData.CAN_CREATE:
            uid = self.odoo.connect()
            result = self.odoo.write(
                uid=uid, model='res.partner', action='create',
                data=DummieData.NEW_PARTNER_DATA)
            self.assertIsNotNone(result)
            self.assertGreater(result, 0)
            self.assertGreater(uid, 0)
        else:
            self.assertFalse(DummieData.CAN_CREATE)

    def test_calling_update_method(self):
        """
        Test the update method using the OdooConnector class.
        :return: None
        """
        if DummieData.CAN_UPDATE and DummieData.ID_TO_UPDATE > 0:
            data = [[DummieData.ID_TO_UPDATE], DummieData.UPDATE_PARTNER_DATA]
            uid = self.odoo.connect()
            result = self.odoo.write(
                uid=uid, model='res.partner', action='write', data=data)
            self.assertIsNotNone(result)
            self.assertGreater(result, 0)
            self.assertGreater(uid, 0)
        else:
            self.assertEqual(DummieData.ID_TO_UPDATE, 0)
            self.assertFalse(DummieData.CAN_UPDATE)

    def test_calling_unlink_method(self):
        """
        Test the delete method using the OdooConnector class.
        :return: None
        """
        if DummieData.CAN_DELETE and DummieData.ID_TO_DELETE > 0:
            uid = self.odoo.connect()
            data = [DummieData.ID_TO_DELETE]
            result = self.odoo.write(
                uid=uid, model='res.partner', action='unlink', data=data)
            self.assertIsNotNone(result)
            self.assertGreater(result, 0)
            self.assertGreater(uid, 0)
        else:
            self.assertEqual(DummieData.ID_TO_DELETE, 0)
            self.assertFalse(DummieData.CAN_DELETE)

    def test_calling_signup_method(self):
        """
        Test the signup method using the OdooConnector class.
        :return: None
        """
        if DummieData.CAN_SIGNUP:
            data = DummieData.NEW_USER_DATA
            uid = self.odoo.connect()
            result = self.odoo.write(
                uid=uid, model='res.users', action='signup', data=data)
            self.assertIsNotNone(result)
            self.assertGreater(len(result), 0)
            self.assertGreater(uid, 0)
        else:
            self.assertFalse(DummieData.CAN_SIGNUP)

    def test_calling_search_method(self):
        """
        Test calling the search method using the OdooConnector  class.
        :return: None
        """
        uid = self.odoo.connect()
        result = self.odoo.search(
            uid=uid, model='res.partner', action='search',
            queries=DummieData.QUERY_FILTER, parameters=None)
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)
        self.assertGreaterEqual(uid, 0)

    def test_calling_search_with_pagination_method(self):
        """
        Test calling the search method using pagination with the OdooConnector class.
        :return: None
        """
        uid = self.odoo.connect()
        result = self.odoo.search(
            uid=uid, model='res.partner', action='search',
            queries=DummieData.QUERY_FILTER,
            parameters={'offset': 2, 'limit': 3})
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)
        self.assertGreaterEqual(uid, 0)

    def test_calling_check_access_rights_method(self):
        """
        Test to call the method "check_access_rights" using the OdooConnector class.
        :return: None
        """
        uid = self.odoo.connect()
        result = self.odoo.search(
            uid=uid, model='res.partner', action='check_access_rights',
            queries=DummieData.PERMISSIONS, parameters={'raise_exception': False})
        self.assertIsNotNone(result)
        self.assertGreater(uid, 0)

    def test_calling_search_count_method(self):
        """
        Test the search_count method using the OdooConnector class.
        :return: None
        """
        uid = self.odoo.connect()
        result = self.odoo.search(
            uid=uid, model='res.partner', action='search_count',
            queries=DummieData.QUERY_FILTER)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(uid, 0)
        self.assertGreaterEqual(result, 0)

    def test_calling_read_method(self):
        """
        Test the read method using the OdooConnector class.
        :return: None
        """
        result = []
        uid = self.odoo.connect()
        ids = self.odoo.search(
            uid=uid, model='res.partner', action='search',
            queries=DummieData.QUERY_FILTER, parameters={'limit': 1})
        if len(ids) > 0:
            result = self.odoo.search(
                uid=uid, model='res.partner', action='read', queries=ids)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(len(result), 0)
        self.assertGreater(uid, 0)

    def test_calling_read_with_fields_selected_method(self):
        """
        Test the read method using the OdooConnector class.
        :return: None
        """
        result = []
        uid = self.odoo.connect()
        ids = self.odoo.search(
            uid=uid, model='res.partner', action='search',
            queries=DummieData.QUERY_FILTER, parameters={'limit': 1})
        if len(ids) > 0:
            result = self.odoo.search(
                uid=uid, model='res.partner', action='read',
                queries=ids, parameters={'fields': DummieData.PARTNER_FIELDS})
        self.assertIsNotNone(result)
        self.assertGreaterEqual(len(result), 0)
        self.assertGreater(uid, 0)

    def test_calling_fields_get_method(self):
        """
        Test the fields_get method using the OdooConnector class.
        :return: None
        """
        result = []
        uid = self.odoo.connect()
        result = self.odoo.search(
            uid=uid, model='res.partner', action='fields_get', queries=[],
            parameters={'attributes': DummieData.FIELD_ATTRIBUTES})
        self.assertIsNotNone(result)
        self.assertGreaterEqual(len(result), 0)
        self.assertGreater(uid, 0)

    def test_calling_search_read_without_parameters_method(self):
        """
        Test the search_read method using the OdooConnector class.
        :return: None
        """
        uid = self.odoo.connect()
        result = self.odoo.search(
            uid=uid, model='res.partner', action='search_read',
            queries=DummieData.QUERY_FILTER, formatted=True)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(len(result), 0)
        self.assertGreater(uid, 0)

    def test_calling_search_read_only_fields_method(self):
        """
        Test the search_read method using the OdooConnector class.
        :return: None
        """
        uid = self.odoo.connect()
        result = self.odoo.search(
            uid=uid, model='res.partner', action='search_read',
            queries=DummieData.QUERY_FILTER,
            parameters={'fields': DummieData.PARTNER_FIELDS}, formatted=True)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(len(result), 0)
        self.assertGreater(uid, 0)

    def test_calling_search_read_only_fields_and_limit_method(self):
        """
        Test the search_read method using the OdooConnector class.
        :return: None
        """
        uid = self.odoo.connect()
        result = self.odoo.search(
            uid=uid, model='res.partner', action='search_read',
            queries=DummieData.QUERY_FILTER,
            parameters={'fields': DummieData.PARTNER_FIELDS, 'limit': 3},
            formatted=True)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(len(result), 0)
        self.assertGreater(uid, 0)

    def test_calling_search_read_with_parameters_method(self):
        """
        Test the search_read method using the OdooConnector class.
        :return: None
        """
        uid = self.odoo.connect()
        result = self.odoo.search(
            uid=uid, model='res.partner', action='search_read',
            queries=DummieData.QUERY_FILTER,
            parameters={'fields': DummieData.PARTNER_FIELDS, 'limit': 2, 'offset': 2},
            formatted=True)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(len(result), 0)
        self.assertGreater(uid, 0)

    def test_any_method(self):
        """
        Test any method existing on the Odoo instance using the OdooConnector class.
        :return: None
        """
        if DummieData.ID_TO_SELECT > 0:
            uid = self.odoo.connect()
            result = self.odoo.search(
                uid=uid, model='res.partner', action='name_get',
                queries=[[DummieData.ID_TO_SELECT]])
            self.assertIsNotNone(result)
            self.assertGreater(len(result), 0)
            self.assertGreater(uid, 0)
        else:
            self.assertEqual(DummieData.ID_TO_SELECT, 0)