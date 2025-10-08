import configparser 
import os
import asyncio

config = configparser.ConfigParser()
config.read("konfiguratsionnyy fayl.ini")

T = config["SETTINGS"]["package"]
if T=="T1":
    from Translator import T1
    translator = T1

if T=="T2":
    from Translator import T2
    translator = T2

if T=="T3":
    from Translator import T3
    translator = T3

def count_file_metrics(file_path):
    C1 = int(config["SETTINGS"]["C1"])
    C2 = int(config["SETTINGS"]["C2"])
    C3 = int(config["SETTINGS"]["C3"])

    if not os.path.isfile(file_path):
        print(f"The file {file_path} does not exist.")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        content = ''
        num_characters = 0
        num_words = 0
        num_sentences = 0

        for line in file:
            content += line
            num_characters += len(line)
            num_words += len(line.split())
            sentences = line.split('.')
            sentences = [s.strip() for s in sentences if s.strip()]
            num_sentences += len(sentences)

            if (num_characters > C1 or
                num_words > C2 or
                num_sentences > C3):
                break
    file_size = os.path.getsize(file_path)
    print(f"розмір файлу: {file_size} bytes")
    print(f"кількість символів: {num_characters}")
    print(f"кількість слів: {num_words}")
    print(f"кількість речень: {num_sentences}")
    print(f"мову тексу: {translator.LangDetect(content) if T!="T1" else asyncio.run(translator.LangDetect(content))}")
    return content

text_file = config["SETTINGS"]["text_file"]

text = count_file_metrics(text_file)

out = config["SETTINGS"]["out"]
dest = config["SETTINGS"]["dest"]

if out=="screen":
    print(f"переклад тексу: {dest}")
    print(f"package: {T}")
    print(translator.TransLate(text=text, dest=dest) if T!="T1" else asyncio.run(translator.TransLate(text=text, dest=dest)))

if out=="file":
    with open("translated_"+dest+".txt", "w", encoding='utf-8') as LNfile:
        print(translator.TransLate(text=text, dest=dest) if T!="T1" else asyncio.run(translator.TransLate(text=text, dest=dest)), file=LNfile)
        print("Ok")


