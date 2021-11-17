import unittest

from  Device import *



class DeviceTestCase(unittest.TestCase):
    def test_open_device(self):
        self.assertIsInstance(open_device('/devices/dev0'), Device)
        self.assertIsInstance(open_device('/devices/dev1'), Device)
        self.assertIsInstance(open_device('/devices/dev2'), Device)
        self.assertIsInstance(open_device('/devices/dev3'), Device)
        self.assertIsInstance(open_device('/devices/dev4'), Device)

        self.assertRaises(IOError, open_device, '/devices/unknown')

    def test_read_line(self):
        self.assertEqual('line_1', read_line(open_device('/devices/dev0')))
        self.assertRaises(PermissionError, read_line, open_device('/devices/dev1'))
        self.assertRaises(IOError, read_line, open_device('/devices/dev2'))
        self.assertEqual('1', read_line(open_device('/devices/dev3')))
        self.assertEqual('line_1', read_line(open_device('/devices/dev4')))


if __name__ == '__main__':
    unittest.main()