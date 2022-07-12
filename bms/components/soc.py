from typing import Dict, Tuple
from bms.components.base import BaseComponent


# SOC Component of the Battery Management System
class SOC(BaseComponent):

    def __init__(self, soc):
        super().__init__(soc)

        # Initialize the value range of temperature
        self.value_range = {(0, 20): ("ERROR SOC is below threshold", False),
                            (21, 24): ("WARNING SOC is approaching lower threshold", True),
                            (24, 75): ("INFO SOC is within limits", True),
                            (76, 80): ("WARNING SOC is approaching upper threshold", True),
                            (81, 100): ("ERROR SOC is above threshold", False)}


