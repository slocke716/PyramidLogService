from logservice.tests.base_test import BaseTestCase
from logservice.scripts.initializedb import InitializeDb


class FunctionalTests(BaseTestCase):

    def test_initialize_db(self):
        init = InitializeDb('', dbsession=self.dbsession)
        init.initialize_db()

    # def test_create_log(self):
    #     init = InitializeDb('', dbsession=self.dbsession)
    #     init.initialize_db()

    def test_get_collection(self):
        init = InitializeDb('', dbsession=self.dbsession)
        init.initialize_db()
        from logservice.log import Log
        lg = Log(self.dbsession)
        col = lg.get_collection()
        length = len(col)
        assert(length > 0)
