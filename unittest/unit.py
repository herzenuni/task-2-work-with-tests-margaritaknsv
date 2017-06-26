import json
import unittest

filename ='data.json'

def tsk(filename):
    with open(filename, encoding='utf-8') as data_file:
        data = json.load(data_file)
    return data

if __name__ == '__main__':
    class TestJSONfile(unittest.TestCase):
        def test_normal_values(self):
            self.assertNotEqual(tsk(filename), FileNotFoundError)

if __name__ == '__main__':
    unittest.main()
