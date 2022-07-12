

# Function to create a test object for various test cases
from bms.battery_management_system import BatteryManagementSystem


def setup_bms(temperature, soc, charge_rate):
    bms = BatteryManagementSystem(temperature, soc, charge_rate)
    return bms


# Test Temperature limits
def test_temperature_less_than_zero():
    test_bms = setup_bms(-1, 30, 0.7)
    assert test_bms.temperature.check_value_status()[1] is False


def test_temperature_more_than_45():
    test_bms = setup_bms(46, 30, 0.7)
    assert test_bms.temperature.check_value_status()[1] is False


def test_temperature_ok():
    test_bms = setup_bms(30, 30, 0.7)
    assert test_bms.temperature.check_value_status()[1] is True


# Test SOC limits
def test_soc_less_than_20():
    test_bms = setup_bms(30, 19, 0.7)
    assert test_bms.soc.check_value_status()[1] is False


def test_soc_more_than_80():
    test_bms = setup_bms(30, 90, 0.7)
    assert test_bms.soc.check_value_status()[1] is False


def test_soc_ok():
    test_bms = setup_bms(45, 30, 0.7)
    assert test_bms.soc.check_value_status()[1] is True


# Test Charge rate limits
def test_cr_more_than_80():
    test_bms = setup_bms(20, 30, 0.9)
    assert test_bms.charge_rate.check_value_status()[1] is False


def test_cr_ok():
    test_bms = setup_bms(20, 30, 0.7)
    assert test_bms.charge_rate.check_value_status()[1] is True


# Test Battery is ok
def test_battery_is_ok():
    test_bms = setup_bms(25, 35, 0.75)
    assert test_bms.overall_health() is True


def test_battery_is_not_ok():
    test_bms = setup_bms(0, 0, 0)
    assert test_bms.overall_health() is False

