import logging
import unittest

logger = logging.getLogger(__name__)


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        ## Override with your setUp method
        pass

    def tearDown(self):
        ## Override with your tearDown method
        pass
