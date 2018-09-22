from abc import ABCMeta, abstractmethod, abstractproperty


class OdooProtocol():
    __metaclass__ = ABCMeta

    def set_link_type(self, value):
        """
        Initialize the endpoint type to connect with Odoo instance
        :param value: string
        :return: None
        """
        self.link_type = value

    def get_link_type(self):
        """
        Return the endopint type to connect with Odoo instance.
        :return: string
        """
        return self.link_type

    link_type = abstractproperty(get_link_type, set_link_type)

    def set_username(self, value):
        """
        Initialize the username to connect with Odoo instance.
        :param value: string
        :return: None
        """
        self.username = value

    def get_username(self):
        """
        return the username used to connect with Odoo instance
        :return: string
        """
        return self.username

    username = abstractproperty(get_username, set_username)

    def set_password(self, value):
        """
        Initialize the password to connect with Odoo instance
        :param value: string
        :return: None
        """
        self.password = value

    def get_password(self):
        """
        return the password to connect with Odoo instance.
        :return: string
        """
        return self.password

    password = abstractproperty(get_password, set_password)

    def set_endpoint(self, value):
        """
        Initialize the endpoint  to connect with Odoo instance.
        :param value: string
        :return: None
        """
        self.endpoint = value

    def get_endpoint(self):
        """
        Return the endpoint to connect with Odoo Instance
        :return: string
        """
        return self.endpoint

    endpoint = abstractproperty(get_endpoint, set_endpoint)

    def set_dbname(self, value):
        """
        Set the database name on the Odoo Connection
        :param value: string
        :return: None
        """
        self.dbname = value

    def get_dbname(self):
        """
        Return the database name on the Odoo Connection
        :return: string
        """
        return self.dbname

    dbname = abstractproperty(get_dbname, set_dbname)

    @abstractmethod
    def link(self, link_type='common'):
        """
        Build the connection link with Odoo instance
        :param link_type: string (endpoint type to connect by default is 'common')
        :return: object (connection link with Odoo instance)
        """
        raise NotImplementedError()

    @abstractmethod
    def connect(self, dbname=None, username=None, password=None):
        """
        Connect with Odoo instance
        :param dbname: string (database name to connect with the Odoo instance)
        :param username: string (username to connect with the Odoo instance)
        :param password: string (password to connect with the Odoo instance)
        :return: int (UID from the user connected.)
        """
        raise NotImplementedError()

    @abstractmethod
    def write(self, uid, model, action, data, password=None):
        """
        Universal method to create, update, signup, unlink methods from Odoo connection
        :param uid: int (UID from the Odoo user connected)
        :param model: string (the name from the model to call on the method)
        :param action: string (the action required to call on the Odoo Web API method.)
        :param data: list (by default is None, they are the data to send to the Web API methods.)
        :param password: string (by default is None, the password to execute the Odoo Web API method.)
        :return: dictionaries list (result from the method called from the Odoo Web API.)
        """
        raise NotImplementedError()

    @abstractmethod
    def search(self, uid, model, action, password=None, queries=None, parameters=None, formatted=False):
        """
        Universal method to Execute or call the methods availables on the Odoo Web API.
        :param uid: int (UID from the Odoo user connected)
        :param model: string (the name from the model to call on the method)
        :param action: string (the action required to call on the Odoo Web API method.)
        :param password: string (by default is None, the password to execute the Odoo Web API method.)
        :param queries: list (by default is None, they are the queries to filter on the Odoo Web API method.)
        :param parameters: list (by default is None, the list from parameters passed by position)
        :param formatted: boolean (by default is False, change to True if you want format the result)
        :return: dictionaries list (result from the method called from the Odoo Web API.)
        """
        raise NotImplementedError()