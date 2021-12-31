programing_languages = ["Programing", "python", "tutorial", "html", "css"]

list_new = programing_languages.copy()

programing_languages.append(1)
programing_languages.insert(0, "Mohamed")
programing_languages.remove("Mohamed")
programing_languages.pop()
programing_languages.index("Programing")
programing_languages.count("Programing")
programing_languages.sort()

print(list_new)
print(programing_languages.index("Programing"))
print(programing_languages)
print(programing_languages.count("Programing"))