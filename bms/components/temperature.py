from typing import Dict, Tuple
from bms.components.base import BaseComponent


# Temperature Component of the Battery Management System
class Temperature(BaseComponent):

    def __init__(self, temperature):
        super().__init__(temperature)

        # Initialize the value range of temperature
        self.value_range = {(-50, 0): ("ERROR Temperature is below threshold", False),
                            (1, 2): ("WARNING Temperature is approaching lower threshold", True),
                            (3, 43): ("INFO Temperature is within limits", True),
                            (44, 45): ("WARNING Temperature is approaching upper threshold", True),
                            (45, 100): ("ERROR Temperature is above threshold", False)}



