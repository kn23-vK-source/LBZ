import json
import os
import T1
import asyncio

def zav1(nlist, Lang):
    if len(nlist)%2!=0:
        print(asyncio.run(T1.TransLate(text="Не введено два цілих числа", dest=Lang)))
        exit(1)

    y1=0
    y2=0
    for x in nlist:
        y1 = y1 + x*x
        y2 = y2 = y2 + x

    print(asyncio.run(T1.TransLate(text="Сума квадратів:", dest=Lang)), end=" ")
    for i in range(int(len(nlist)/2)):
        print(f"{nlist[i]}^2+{nlist[i+1]}^2", end="")
        if i < int(len(nlist)/2)-1:
            print("+", end="")

    print(f"={y1}", end="")

    print()
    print(asyncio.run(T1.TransLate(text="Квадрат суми:", dest=Lang)), end=" ")
    print("(", end="")

    for i in range(int(len(nlist)/2)):
        print(f"{nlist[i]}+{nlist[i+1]}", end="")
        if i < int(len(nlist)/2)-1:
            print("+", end="")

    print(f")^2={y2*y2}")

    if(y1>y2*y2):
        print(asyncio.run(T1.TransLate(text="Квадрат суми більше!", dest=Lang)))
    else:
        print(asyncio.run(T1.TransLate(text="Сума квадратів більше!", dest=Lang)))



file_path = 'MyData.json'
MyData:dict = {}
nlist = []

if os.path.exists(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            MyData = json.load(json_file)

            print(asyncio.run(T1.TransLate(text="Мова:", dest=MyData["Lang"])), 
                  T1.CodeLang(MyData["Lang"]))
            
            print(asyncio.run(T1.TransLate(text="Два цілих числа:", dest=MyData["Lang"])), end="")
            for i in range(MyData["Size"]):
                nlist.append(MyData[str(i)])
                print(MyData[str(i)], end=" ")
            print()
            zav1(nlist, MyData["Lang"])


    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from file {file_path}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
else:
    print(f"The file {file_path} does not exist.")
    ninput = input("Введіть два цілих числа: ")

    Lang = input("Введіть мову інтерфейсу: ")

    if T1.CodeLang(Lang) == "Error":
        Lang = "uk"

    MyData["Lang"] = Lang

    ninput = list(map(int, ninput.split()))
    Size = 0
    for i in range(len(ninput)):
        MyData[i]=ninput[i]
        Size = Size + 1
    
    MyData["Size"] = Size

    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(MyData, json_file, ensure_ascii=False, indent=4)

    print(asyncio.run(T1.TransLate(text="Дані записані у файл MyData.json", dest=Lang)))