# Creating a class for BMS with temperature, soc, charge_rate as encapsulated fields
class BatteryManagementSystem:
    def __init__(self):
        self.temperature = None
        self.soc = None
        self.charge_rate = None

    def set_temperature(self, temperature):
        self.temperature = temperature

    def set_soc(self, soc):
        self.soc = soc

    def set_charge_rate(self, charge_rate):
        self.charge_rate = charge_rate

    def temperature_is_ok(self):
        if self.temperature < 0 or self.temperature > 45:
            print("Temperature is out of range")
            return False
        return True

    def soc_is_ok(self):
        if self.soc < 20 or self.soc > 80:
            print("State of Charge is out of range!")
            return False
        return True

    def charge_rate_is_ok(self):
        if self.charge_rate > 0.8:
            print("Charge rate is out of range!")
            return False
        return True

    def battery_is_ok(self):
        if self.temperature_is_ok() and self.soc_is_ok() and self.charge_rate_is_ok():
            print("Battery is ok")
            return True

        return False


if __name__ == '__main__':
    # Testing sample BMS examples
    bms1 = BatteryManagementSystem()
    bms1.set_temperature(25)
    bms1.set_soc(70)
    bms1.set_charge_rate(0.7)

    assert(bms1.battery_is_ok() is True)

    bms2 = BatteryManagementSystem()
    bms2.set_temperature(50)
    bms2.set_soc(85)
    bms2.set_charge_rate(0)

    assert (bms2.battery_is_ok() is False)