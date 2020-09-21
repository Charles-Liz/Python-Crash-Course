import unittest
from city_country import get_city_country
class NamesTestCase(unittest.TestCase):
    def test_city_country(self):
        '''能够正确返回字符串吗'''
        name = get_city_country('Santiago', 'Chile')
        self.assertEqual(name,'Santiago,Chile')

unittest.main()
