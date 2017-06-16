import unittest

from make_dataset import main


class TestMain(unittest.TestCase):

    def test_main_runs(self):
        self.assertTrue(main())

