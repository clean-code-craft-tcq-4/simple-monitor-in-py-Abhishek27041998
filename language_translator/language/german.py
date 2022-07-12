# German Language Translator
from language_translator.translator import LanguageTranslator


class GermanLanguageTranslator(LanguageTranslator):
    """
    German language translator
    """
    def __init__(self, source, destination):
        super().__init__(source, destination)

        self.translations = dict()
        self.translations["ERROR Temperature is below threshold"] = "FEHLER Die Temperatur liegt unter dem Schwellenwert"
        self.translations["WARNING Temperature is approaching lower threshold"] = "WARNUNG Die Temperatur nähert sich dem unteren Schwellenwert"
        self.translations["INFO Temperature is within limits"] = "INFO Temperatur innerhalb der Grenzen"
        self.translations["WARNING Temperature is approaching upper threshold"] = "WARNUNG Die Temperatur nähert sich dem oberen Schwellenwert"
        self.translations["ERROR Temperature is above threshold"] = "FEHLER Temperatur liegt über dem Schwellenwert"
        self.translations["ERROR SOC is below threshold"] = "FEHLER SOC liegt unter dem Schwellenwert"
        self.translations["WARNING SOC is approaching lower threshold"] = "WARNUNG SOC nähert sich dem unteren Schwellenwert"
        self.translations["INFO SOC is within limits"] = "INFO SOC hält sich in Grenzen"
        self.translations["WARNING SOC is approaching upper threshold"] = "WARNUNG SOC nähert sich dem oberen Schwellenwert"
        self.translations["ERROR SOC is above threshold"] = "FEHLER SOC liegt über dem Schwellenwert"
        self.translations["WARNING ChargeRate is approaching threshold"] = "WARNUNG ChargeRate nähert sich dem Schwellenwert"
        self.translations["INFO ChargeRate is within limits"] = "INFO ChargeRate hält sich in Grenzen"
        self.translations["ERROR ChargeRate is above threshold"] = "ERROR ChargeRate liegt über dem Schwellenwert"

