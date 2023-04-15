ranked_dictionary = {}
with open("../data/iot_lib_map_ranked.txt", "r", encoding='utf-8') as packages_names:
    packages = packages_names.readlines()
    for package in packages:
        line = eval(package)
        if len(line["apps"]) == 0:
            ranked_dictionary[str(line["package_name"])] = 0
        else:
            ranked_dictionary[str(line["package_name"])] = len(line["apps"])

ranked_dictionary = sorted(ranked_dictionary.items(), key=lambda x:x[1], reverse=True)
with open("../data/iot_libraries_ranked.txt", "a", encoding="utf-8") as file:
    for i in ranked_dictionary:
        file.write(str(i) + "\n")