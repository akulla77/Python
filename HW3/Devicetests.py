import unittest

from  Device import *



class DeviceTestCase(unittest.TestCase):
    def test_open_device(self):
        self.assertIsInstance(open_device('/devices/dev0'), Device) #r
        self.assertIsInstance(open_device('/devices/dev1'), Device) #w
        self.assertIsInstance(open_device('/devices/dev2'), Device) #rw
        self.assertIsInstance(open_device('/devices/dev3'), Device) #rw
        self.assertIsInstance(open_device('/devices/dev4'), Device) #r
        self.assertRaises(IOError, open_device, '/devices/unknown')

    def test_read_line(self):
        self.assertEqual('line_1', read_line(open_device('/devices/dev0')))
        self.assertRaises(PermissionError, read_line, open_device('/devices/dev1'))
        self.assertRaises(IOError, read_line, open_device('/devices/dev2'))
        self.assertEqual('1', read_line(open_device('/devices/dev3')))
        self.assertEqual('line_1', read_line(open_device('/devices/dev4')))


    def test_write_line(self):
        self.assertRaises(PermissionError, write_line, open_device('/devices/dev0'), 'Python')
        d = open_device('/devices/dev2')
        write_line(d,'Python')
        self.assertEqual('Python', read_line(d))


if __name__ == '__main__':
    unittest.main()