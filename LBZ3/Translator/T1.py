import asyncio
from googletrans import Translator
from googletrans import LANGUAGES

async def TransLate(text : str, scr : str="auto", dest : str="en") -> str:
    async with Translator() as translator:
        result = await translator.translate(text,src=scr.title(), dest=dest.title())
        return result.text

async def LangDetect(text : str, set : str="all") -> str:
    async with Translator() as translator:
        result = await translator.detect(str)
        if set == "lang":
            return result.lang
        elif set == "confidence":
            return str(result.confidence)
        elif set == "all":
            return result
        else:
            return "Невірний параметр set"

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

def LanguageList(out : str="screen", text : str="") -> str:
    if out == "screen":
        print("N".ljust(10), "Language".ljust(35), "ISO-639 code".ljust(15), "Text" if text!="" else "")
        print("-" * 95)
        index = 1

        for code, language in LANGUAGES.items():
            print(f"{index}".ljust(10), language.title().ljust(35), code.ljust(15), asyncio.run(TransLate(text=text, dest=code)) if text!="" else "")
            index = index + 1
            if index > 6:
                print("." * (32))
                print("Ok")
                break

    if out == "file":
        with open("translated.txt", "w", encoding='utf-8') as LNfile:
            print("N".ljust(10), "Language".ljust(35), "ISO-639 code".ljust(15), "Text" if text!="" else "", file=LNfile)
            print("-" * 95, file=LNfile)
            index = 1

            for code, language in LANGUAGES.items():
                source = asyncio.run(TransLate(text=text, dest=code))

                print(f"{index}".ljust(10), language.title().ljust(35), code.ljust(15), source if text!="" else "", file=LNfile)
                index = index + 1
                if index > 6:
                    print("." * (32), file=LNfile)
                    print("Ok", file=LNfile)
                    break

    return "Ok"