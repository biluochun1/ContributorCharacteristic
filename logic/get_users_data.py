import time

from github import github
import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
param = {
    "access_token": "fe02456ecf2d54f585e1899d677bc41beeda2e23"
}
headers = {
    'Connection': 'close'
}

# project_list = ["babel","bitcoin","bootstrap", "cocos2d", "ffmpeg", "flask", "flutter", "kubernetes", "opencv",
#                 "pytorch", "redis", "threejs", "tidb", "vue"]
project_list = ["kubernetes", "opencv",
                "pytorch", "redis", "threejs", "tidb", "vue"]

s = requests.session()
s.params = param


def str2json(s):
    return json.loads(s.decode("utf-8"), encoding="utf-8")


#
# def get_user_data(username):
#     g = github.Github(username=username, password=password)
#     _, r = g.users.getUser(username)
# user_dict = json.loads(r["body"].decode("utf-8"), encoding="utf-8")
# print(r)
# resp = g.events.listRepoEvents(repo="grpc",user="Craig Tiller")
# print(resp)


def save_file(project_name):
    users_data = []
    count = 0
    with open(
            "/Users/weizijian/PycharmProjects/ContributerCharacteristics/data/contributors_data/" + project_name + "_contributors.json",
            "r", encoding="utf-8") as f:
        with open(
                "/Users/weizijian/PycharmProjects/ContributerCharacteristics/data/users_data/" + project_name + "_users_data.json",
                "w") as fw:
            data = json.load(f)
            for e in data:
                count += 1
                # r = requests.get(e['url'], params=param, headers=headers, verify=False)
                r = s.get(url=e["url"], verify=False)
                print(project_name + " count|" + str(count) + "|" + r.url)
                print(r.json())
                users_data.append(r.json())
            fw.write(json.dumps(users_data))


def parsing_data(path="data/spark_users_data.json", field="company"):
    count_list = []
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        for e in data:
            if e[field] is not None:
                count_list.append(e[field])
            else:
                count_list.append("default")
        print(count_list)
        print(len(count_list))
    _, l1, l2 = use_list_count(count_list)
    print(l1, l2)
    return l1, l2


def use_list_count(l: list, num: int = 6):
    count_set = set(l)
    count_list = []
    l1 = []
    l2 = []
    for item in count_set:
        count_list.append((l.count(item), item))
    sort_count_list = sorted(count_list)
    print(sort_count_list)
    l1, l2 = rm_dumplicate_element(sort_count_list)

    return count_list, l1, l2


def rm_dumplicate_element(l: list):
    res = []
    l1 = []
    l2 = []
    tmp = []
    # flag = [False] * len(l)
    for i in range(len(l)):
        key = l[i][1]
        count = l[i][0]
        for j in range(len(l)):
            if j != i:
                if str(l[j][1]).lower() in str(key).lower() or str(key).lower() in str(l[j][1]).lower():
                    count += l[j][0]

        res.append((count, key))
    res = sorted(res)
    for i in range(len(res) - 2, -1, -1):
        l1.append(res[i][0])
        l2.append(res[i][1])
        tmp.append(res[i][1])

    print(l1, l2)
    for i in range(len(tmp)):
        key = tmp[i]
        for j in range(i + 1, 9):
            if str(tmp[j]).lower().strip() in str(key).lower().strip() or str(key).lower().strip() in str(
                    tmp[j]).lower().strip():
                l1.pop(j)
                l2.pop(j)
    print(l1, l2)
    return l1, l2


if __name__ == '__main__':
    for e in project_list:
        save_file(e)
