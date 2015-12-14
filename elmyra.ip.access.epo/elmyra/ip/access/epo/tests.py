import unittest
from pyramid import testing

class TestMyView(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_it(self):
        from .views import navigator_standalone
        request = testing.DummyRequest()
        info = navigator_standalone(request)
        self.assertEqual(info['project'], 'elmyra.ip.access.epo')
