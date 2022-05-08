from unittest import TestCase
from context import src
from src.my_module import get_cheapest_hotel


class MyTest(TestCase):
    def test1(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"))

    def test2(self):
        result = "Bridgewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))

    def test3(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"))

    def test4(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 08May2022(sun), 09May2022(mon), 10May2022(tues), "
                                                    "11May2022(wed), 12May2022(thur)"))

    def test5(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 08May2022(sun), 09May2022(mon), 10May2022(tues), "
                                                    "11May2022(wed), 12May2022(thur)"))

    def test6(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 09May2022(mon), 10May2022(tues), 11May2022(wed), "
                                                    "12May2022(thur), 13May2022(fri)"))

    def test7(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 06May2022(fri), 07May2022(sat)"))

    def test8(self):
        result = "Bridgewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 13May2022(fri), 14May2022(sat), 15May2022(sun), "
                                                    "20May2022(fri), 21May2022(sat), 22May2022(sun), 27May2022(fri)"
                                                    "28May2022(sat)"))
