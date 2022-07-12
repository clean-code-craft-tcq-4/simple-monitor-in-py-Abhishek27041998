from typing import Dict, Tuple


# Base Class for deriving the other components related to Battery Management
# System like Temperature, SOC, Charge Rate etc
class BaseComponent:

    # Common data structure to store the value ranges and breach messages, status
    # Eg : {(0, 20) -> ("LOW_SOC_BREACH", False), (20, 80) -> ("LOW_SOC_WARNING", True) ...}
    value_range: Dict[Tuple, Tuple]

    def __init__(self, value):
        self.value = value

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def check_value_status(self):
        # Check the value with reference to ranges and return appropriate message
        for range in self.value_range.keys():
            if range[0] <= self.value <= range[1]:
                return self.value_range[range]

