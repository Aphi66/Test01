import unittest

class RoomBillCalculator:
    SINGLE_ROOM_COST = 1500
    DOUBLE_ROOM_COST = 2000
    WATER_RATE = 5
    ELECTRICITY_RATE = 6

    def __init__(self, last_water_meter, current_water_meter, last_elect_meter, current_elect_meter):
        self.last_water_meter = last_water_meter
        self.current_water_meter = current_water_meter
        self.last_elect_meter = last_elect_meter
        self.current_elect_meter = current_elect_meter

    def calculate_water_bill(self):
        if self.current_water_meter >= self.last_water_meter:
            return (self.current_water_meter - self.last_water_meter) * self.WATER_RATE
        raise ValueError("Current water meter reading cannot be less than last reading.")

    def calculate_elect_bill(self):
        if self.current_elect_meter >= self.last_elect_meter:
            return (self.current_elect_meter - self.last_elect_meter) * self.ELECTRICITY_RATE
        raise ValueError("Current electricity meter reading cannot be less than last reading.")

    def calculate_total_bill(self, room_type):
        if room_type.lower() == "s":
            room_cost = self.SINGLE_ROOM_COST
        elif room_type.lower() == "d":
            room_cost = self.DOUBLE_ROOM_COST
        else:
            raise ValueError("Invalid room type. Use 's' for single or 'd' for double.")
        return room_cost + self.calculate_water_bill() + self.calculate_elect_bill()



class TestRoomBillCalculator(unittest.TestCase):

    def test_calculate_water_bill(self):
        calculator = RoomBillCalculator(50, 100, 0, 0)
        self.assertEqual(calculator.calculate_water_bill(), 250)

    def test_calculate_elect_bill(self):
        calculator = RoomBillCalculator(0, 0, 20, 50)
        self.assertEqual(calculator.calculate_elect_bill(), 180)

    def test_calculate_total_bill_single_room(self):
        calculator = RoomBillCalculator(50, 100, 20, 50)
        self.assertEqual(calculator.calculate_total_bill("s"), 1930)

    def test_calculate_total_bill_double_room(self):
        calculator = RoomBillCalculator(50, 100, 20, 50)
        self.assertEqual(calculator.calculate_total_bill("d"), 2430)

    def test_invalid_room_type(self):
        calculator = RoomBillCalculator(50, 100, 20, 50)
        with self.assertRaises(ValueError):
            calculator.calculate_total_bill("x")

    def test_invalid_water_meter_reading(self):
        calculator = RoomBillCalculator(100, 50, 20, 50)
        with self.assertRaises(ValueError):
            calculator.calculate_water_bill()

    def test_invalid_elect_meter_reading(self):
        calculator = RoomBillCalculator(50, 100, 50, 20)
        with self.assertRaises(ValueError):
            calculator.calculate_elect_bill()


if __name__ == "__main__":
    unittest.main()
