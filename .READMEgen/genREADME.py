import os

from config import *
from colorama import Fore, Style, Back

lang_names = sorted(list(langs.keys()))

with open(".READMEgen/README.template.md", "r") as f:
    [top, doneel, missel] = f.read().split("@$@sp@$@\n")


README = top
tsize = os.get_terminal_size()[0]
misstext = "-(TOT)-"
t = ((tsize - 2) // len(misstext)) - 2
misstext = misstext * t
colored_misstext = (
    Fore.RED
    + "-("
    + Fore.CYAN
    + "T"
    + Fore.RED
    + "0"
    + Fore.CYAN
    + "T"
    + Fore.RED
    + ")-"
    + Fore.RESET
)
colored_misstext = "".join([colored_misstext] * t)
cmissingcode = (
    misstext.center(tsize - 2).split(misstext)[0]
    + colored_misstext
    + misstext.center(tsize).split(misstext)[1][:-1]
)
print(Back.BLACK)
print(" " + "_" * (tsize - 2) + " ")
print("|" + " " * (tsize - 2) + "|")
print("|" + Fore.BLUE + "GENERATING README".center(tsize - 2) + Fore.RESET + "|")
for n, lang in enumerate(lang_names):
    print("|" + "_" * (tsize - 2) + "|")
    try:
        with open("fib" + langs[lang], "r") as f:
            code = f.read()

        if code != "":
            print("|" + "_" * (tsize - 2) + "|")
            print("|" + "_" * (tsize - 2) + "|")
            print("|" + " " * (tsize - 2) + "|")
            print("|" + Fore.GREEN + lang.center(tsize - 2) + Fore.RESET + "|")
            print("|" + "_" * (tsize - 2) + "|")
            print("|" + "_" * (tsize - 2) + "|")
            print("|" + " " * (tsize - 2) + "|")
            print("|" + " " * (tsize - 2) + "|")
            maxl = max([len(x) for x in code.split("\n")])
            print(
                "\n".join(
                    [
                        "|"
                        + Fore.GREEN
                        + x.ljust(maxl).center(tsize - 2)
                        + Fore.RESET
                        + "|"
                        for x in code.split("\n")
                    ]
                )
            )
            README=README.replace('@$@rd@$@',doneel.replace('@$@1@$@',lang).replace('@$@2@$@',langs[lang]).replace('@$@3@$@',lang.lower()+'\n'+code))
        else:
            print(
                Back.BLACK + "|" + Fore.RED + lang.center(tsize - 2) + Fore.RESET + "|"
            )
            print("|" + "_" * (tsize - 2) + "|")
            print("|" + "_" * (tsize - 2) + "|")
            print("|" + " " * (tsize - 2) + "|")
            print("|" + " " * (tsize - 2) + "|")
            print("|" + cmissingcode + "|")
            README=README.replace('@$@rm@$@\n\n',missel.replace('@$@1@$@',lang).replace('@$@2@$@',langs[lang]))
        print("|" + " " * (tsize - 2) + "|" + Fore.RESET)

    except:
        print("|" + "_" * (tsize - 2) + "|")
        print("|" + "_" * (tsize - 2) + "|")
        print("|" + " " * (tsize - 2) + "|")
        print("|" + Fore.RED + lang.center(tsize - 2) + Fore.RESET + "|")
        print("|" + "_" * (tsize - 2) + "|")
        print("|" + "_" * (tsize - 2) + "|")
        print("|" + " " * (tsize - 2) + "|")
        print("|" + " " * (tsize - 2) + "|")
        print("|" + cmissingcode + "|")
        print("|" + " " * (tsize - 2) + "|")
        README=README.replace('@$@rm@$@',missel.replace('@$@1@$@',lang).replace('@$@2@$@',langs[lang]))


README=README.replace('@$@rd@$@\n\n\n\n\n','')
README=README.replace('@$@rm@$@','')
print("|" + "_" * (tsize - 2) + "|")
print("|" + "_" * (tsize - 2) + "|")
print("|" + " " * (tsize - 2) + "|")
print("|" + Fore.CYAN + "README.md".center(tsize - 2) + Fore.RESET + "|")
print("|" + "_" * (tsize - 2) + "|")
print("|" + "_" * (tsize - 2) + "|")
print("|" + " " * (tsize - 2) + "|")
maxl2 = max([len(x) for x in README.split("\n")])
print(
    "\n".join(
        [
            "|" + Fore.CYAN + x.ljust(maxl2).center(tsize - 2) + Fore.RESET + "|"
            for x in README.split("\n")
        ]
    )
)
print("|" + "_" * (tsize - 2) + "|"+Style.RESET_ALL)
with open('README.md','w') as f:
    f.write(README)