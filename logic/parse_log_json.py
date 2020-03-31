import json
from collections import defaultdict, Counter
from itertools import groupby
import numpy

project_list = ["babel", "bitcoin", "bootstrap", "cocos2d", "ffmpeg", "flask", "flutter", "kubernetes", "opencv",
                "pytorch", "redis", "threejs", "tidb", "vue", "grpc", "spark", "spring"]


def parse_log_json_and_save_file(path="data/git-log-json/grpc_gitlog.json",
                                 out_path="data/git-log-json/grpc-file-analysy.json"):
    file_count_dict = {}
    file_user_dict = defaultdict(set)
    with open(path, "r", encoding="utf-8") as f:
        with open(out_path, "w") as fw:
            data = json.load(f)
            for e in data:
                for change in e["changes"]:
                    if change[2] in file_count_dict:
                        file_count_dict[change[2]] += 1
                    else:
                        file_count_dict[change[2]] = 1
                    file_user_dict[change[2]].add(e["author"]["name"])
            sort_file_count = sorted(file_count_dict.items(), key=lambda item: item[1])
            fw.write(json.dumps(sort_file_count))
            fw.write("\n")
            fw.write(str(dict(file_user_dict)))


def get_vector(
        path="/Users/weizijian/PycharmProjects/ContributerCharacteristics/data/file_analysis_data/pytorch-file-analysy.json"):
    with open(path, "r", encoding="utf-8") as f:
        s = f.read().split("\n")
        j = json.loads(s[0])
        l = list(reversed(list(j)))
        l1 = []
        l2 = []
        l3 = []
        file_user_dict = eval(s[1])
        # print(file_user_dict)
        # print(file_user_dict)
        for i in range(20):
            l1.append(str(l[i][0]).split("/")[-1])
            l2.append(l[i][1])
            l3.append(len(file_user_dict[l[i][0]]))
        print(l2)
        print(l1)
        # count = Counter(l3)
        # key = list(count.keys())
        # val = list(count.values())
        #
        # val,key = sort_two_list(val,key)
        # print(val)
        # print(key)


def sort_two_list(X, Y):
    return [x for _, x in sorted(zip(Y, X))], [y for y, _ in sorted(zip(Y, X))]


if __name__ == '__main__':
    # get_vector()

    country_l = [1709062,
                 428786,
                 319787,
                 304752,
                 250708,
                 151529,
                 143815,
                 109823,
                 108934,
                 104802,
                 101331,
                 90174,
                 75198,
                 60553,
                 53652,
                 51811,
                 51584,
                 46350,
                 44280,
                 36515,
                 35856,
                 32486,
                 30541,
                 29659,
                 27956
                 ]
    # print(sum([408, 351, 297, 246, 246, 227, 218, 200, 184, 181, 151, 149, 148, 141, 139, 137, 127, 126, 125, 123]))
    sum = sum(country_l)
    nl = numpy.asarray(country_l)
    print((nl/sum)*500979)
    # for e in project_list:
    #     outpath = "/Users/weizijian/PycharmProjects/ContributerCharacteristics/data/file_analysis_data/" + e + "-file-analysy.json"
    #     path = "/Users/weizijian/PycharmProjects/ContributerCharacteristics/data/git-log-json/" + e + "-git-log.json"
    #     parse_log_json_and_save_file(path, outpath)
