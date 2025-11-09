import json
from pathlib import Path
from fastapi import Request


class TranslationService:
    def __init__(self):
        self.locales_path = Path(__file__).parent.parent / "locales"
        self.translations = {}
        self.load_translations()

    def load_translations(self):
        for lang_file in self.locales_path.glob("*.json"):
            lang = lang_file.stem
            with open(lang_file, 'r', encoding='utf-8') as f:
                self.translations[lang] = json.load(f)

    def get_translation(self, key: str, language: str = "en") -> str:
        return self.translations.get(language, {}).get(key, key)

    def get_all_translations(self, language: str = "en") -> dict:
        return self.translations.get(language, {})


translation_service = TranslationService()


def get_user_language(request: Request) -> str:
    return request.cookies.get("language", "en")
