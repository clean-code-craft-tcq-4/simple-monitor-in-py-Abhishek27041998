from typing import Dict, Tuple
from bms.components.base import BaseComponent


# ChargeRate Component of the Battery Management System
class ChargeRate(BaseComponent):

    def __init__(self, charge_rate):
        super().__init__(charge_rate)

        # Initialize the value range of temperature
        self.value_range = {(0.76, 0.8): ("WARNING ChargeRate is approaching threshold", True),
                            (0, 0.76): ("INFO ChargeRate is within limits", True),
                            (0.81, 1): ("ERROR ChargeRate is above threshold", False)}


