from Translator import T1
import asyncio

print(T1.CodeLang("Filipino"))
T1.LanguageList("screen", "Hello, world!") 
print(asyncio.run(T1.TransLate("Hello, world!", "en", "uk")))
print(asyncio.run(T1.LangDetect("Hello, world!")))
