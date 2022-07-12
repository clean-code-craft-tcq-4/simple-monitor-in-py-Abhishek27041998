from bms.battery_management_system import BatteryManagementSystem

# Global variable for language
LANGAUGE = "english"  # Can be 'english' or 'german'


if __name__ == '__main__':
    # Testing sample BMS examples
    bms1 = BatteryManagementSystem(25, 70, 0.7)

    assert(bms1.overall_health() is True)

    bms2 = BatteryManagementSystem(50, 85, 0)

    assert (bms2.overall_health() is False)