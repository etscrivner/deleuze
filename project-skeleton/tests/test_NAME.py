from tests import base


class FailingTest(base.BaseTestCase):

    def test_should_fail_to_remind_you_to_write_tests(self):
        """This test fails here to remind you that you need some tests"""
        self.fail('Please write some unit-tests.')
