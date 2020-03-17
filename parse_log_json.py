import json
from collections import defaultdict


def parse_log_json_and_save_file(path="data/git-log-json/grpc_gitlog.json",
                                 out_path="data/git-log-json/grpc-file-analysy.json"):
    file_count_dict = {}
    file_user_dict = defaultdict(list)
    # file_set = set()
    with open(path, "r", encoding="utf-8") as f:
        with open(out_path, "w") as fw:
            data = json.load(f)
            # print(data[0])
            # print(len(data))
            for e in data:
                for change in e["changes"]:
                    # file_set.add(change[2])
                    if change[2] in file_count_dict:
                        file_count_dict[change[2]] += 1
                    else:
                        file_count_dict[change[2]] = 1
                    file_user_dict[change[2]].append(e["author"]["name"])
            sort_file_count = sorted(file_count_dict.items(), key=lambda item: item[1])
            fw.write(json.dumps(sort_file_count))
            fw.write("\n")
            fw.write(json.dumps(file_user_dict))
            # print(file_user_dict["Makefile"])
