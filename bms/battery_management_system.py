from language_translator.language.german import GermanLanguageTranslator

from bms.components.charge_rate import ChargeRate
from bms.components.soc import SOC
from bms.components.temperature import Temperature


# Creating a class for BMS with temperature, soc, charge_rate as encapsulated fields
class BatteryManagementSystem:
    def __init__(self, temperature, soc, charge_rate):
        self.temperature = Temperature(temperature)
        self.soc = SOC(soc)
        self.charge_rate = ChargeRate(charge_rate)

    def overall_health(self):
        # Gather all the status of components
        component_status = [self.temperature.check_value_status(),
                            self.soc.check_value_status(),
                            self.charge_rate.check_value_status()]

        for check in component_status:
            message, status = check
            self.print_status_message(message)
            if status is False:
                return False

        return True

    def print_status_message(self, message: str):
        from check_limits import LANGAUGE
        if LANGAUGE != "english":
            translator = GermanLanguageTranslator(source="english", destination=LANGAUGE)
            message = translator.translate(message)

        print(message)

