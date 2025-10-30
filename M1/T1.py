from googletrans import Translator
from googletrans import LANGUAGES

async def TransLate(text : str, scr : str="auto", dest : str="en") -> str:
    async with Translator() as translator:
        result = await translator.translate(text,src=scr.title(), dest=dest.title())
        return result.text

def CodeLang(lang: str) -> str:
    str_res="Error"
    for code, language in LANGUAGES.items():
        if lang.title() in code.title():
            str_res = language
            break
        if lang.title() in language.title():
            str_res = code
            break
    return str_res