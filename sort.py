dictionary_file = "dictionary.md"
dictionary = {}

with open(dictionary_file, "r") as f:
    for line in f:
        if "=" in line:
            p = line.strip().split("=")
            dictionary[p[0]] = p[1]
        else:
            continue

sorted_keys = sorted(list(dictionary.keys()))

with open(dictionary_file, "w") as f:
    for k in sorted_keys:
        print(k + "=" + dictionary[k], file=f,)