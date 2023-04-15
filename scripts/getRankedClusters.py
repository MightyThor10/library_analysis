ranked_dictionary = {}
with open("../data/cluster_app_mapping.txt", "r", encoding='utf-8') as clusters_names:
    clusters = clusters_names.readlines()
    for cluster in clusters:
        line = eval(cluster)
        if len(line["apps"]) == 0:
            ranked_dictionary[str(line["cluster"])] = 0
        else:
            ranked_dictionary[str(line["cluster"])] = len(line["apps"])

ranked_dictionary = sorted(ranked_dictionary.items(), key=lambda x:x[1], reverse=True)
with open("../data/iot_clusters_ranked.txt", "a", encoding="utf-8") as file:
    for i in ranked_dictionary:
        file.write(str(i) + "\n")