from github import github
import json
import numpy


def str2json(s):
    return json.loads(s.decode("utf-8"), encoding="utf-8")


def run():
    g = github.Github(username=username, password=password)
    _, r = g.users.getUser("Muxi-Yan")
    # user_dict = json.loads(r["body"].decode("utf-8"), encoding="utf-8")
    print(r)
    # resp = g.events.listRepoEvents(repo="grpc",user="Craig Tiller")
    # print(resp)


# def parse_4days_log():
#     with open("/Users/weizijian/Downloads/gray_0305_data.txt", "w+") as fw:
#         with open("/Users/weizijian/Downloads/gray_3days_full.txt", "r") as f:
#             for line in f.readlines():
#                 s = line.split("[")
#                 data = s[1][0:10]
#                 print(data)
#                 vid = s[3].split("|")[1]
#                 l = data + "\t" + vid
#                 fw.write(l)
# print(vid)


def parse_gitlog_json(path="/Users/weizijian/Downloads/bi_she_repo_download/grpc_gitlog.json"):
    log = json.load(open(path))
    print(log[0])


def parse_country_data(path="/Users/weizijian/PycharmProjects/ContributerCharacteristics/logic/contry_data.txt"):
    co = []
    pop = []
    contry = []
    with open(path, "r") as f:
        for line in f.readlines():
            s = line.strip().split("|")
            print(s)
            contry.append(s[0])
            co.append(int(s[1]))
            pop.append(int(s[2]))
    sum_co = sum(co)
    nl = numpy.asarray(co)
    real_co = (nl / 4399944) * 500979
    real_co = numpy.around(real_co, decimals=4)
    numpy.set_printoptions(suppress=True)
    pop = numpy.asarray(pop)
    print(contry)
    print(real_co)
    print(pop)
    print(list(real_co / pop * 10000))


# [59.41822138 39.11870724  9.78939912  8.19009771  7.83208589  7.62020462
#   7.4869807   7.46690032  7.36598026  6.76110281  6.29039917  6.24912348
#   5.90665512  5.82864022  5.79724134  5.40744529  4.47503026  4.31950775
#   4.16977275  3.84049482  3.34982094  3.25296003  3.23615473  2.98495252
#   2.66885922]
def add_path():
    with open("/Users/weizijian/Downloads/false.txt", "r") as f:
        with open("/Users/weizijian/Downloads/false_path.txt", "w") as fw:
            for line in f.readlines():
                name = line.strip().split("\t")[0]
                name = "/data/ceph_11015/sata/hugh/data/frames/sku_0330/" + name.split("_")[0] + "/" + name + "\n"
                print(name)
                fw.write(name)


if __name__ == '__main__':
    # run()
    # parse_4days_log()
    # parse_country_data()
    add_path()
