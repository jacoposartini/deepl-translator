import requests

class DeeplTranslator:
    BASE_URL = "https://api.deepl.com/v2"
    # LANGUAGES
    EN = "EN"  # English
    FR = "FR"  # French
    IT = "IT"  # Italian
    JA = "JA"  # Japanese
    ES = "ES"  # Spanish
    NL = "NL"  # Dutch
    PL = "PL"  # Polish
    PT = "PT"  # Portuguese(all Portuguese varieties mixed)
    RU = "RU"  # Russian
    ZH = "ZH"  # Chinese
    DE = "DE"  # German
    AUTO = None # Auto translate

    def __init__(self, api_key):
        self.api_key = api_key

    def get_info(self):
        try:
            response = requests.get(
                url=f"{self.BASE_URL}/usage", params={'auth_key': self.api_key})
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise SystemExit(e)
        return response.json()

    def translate(self, text="Happy coding!", source_lang=AUTO, target_lang=IT):
        params = {
            'auth_key': self.api_key,
            'text': text,
            'source_lang': source_lang,
            'target_lang': target_lang
        }
        try:
            response = requests.get(
                url=f"{self.BASE_URL}/translate", params=params)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise SystemExit(e)
        translations = response.json()['translations']
        return translations if len(translations) > 1 else translations[0]
