from github import github
import json
import requests

username = "823510561@qq.com"
password = "823510561qq"
suffix = "access_token=78854faee2ae023107ee2699c35d2229d194a36d"

param = {
    "access_token": "78854faee2ae023107ee2699c35d2229d194a36d"
}


def str2json(s):
    return json.loads(s.decode("utf-8"), encoding="utf-8")


def get_user_data(username):
    g = github.Github(username=username, password=password)
    _, r = g.users.getUser(username)
    # user_dict = json.loads(r["body"].decode("utf-8"), encoding="utf-8")
    print(r)
    # resp = g.events.listRepoEvents(repo="grpc",user="Craig Tiller")
    # print(resp)


def save_file():
    users_data = []
    count = 0
    with open("data/spark_contributors.json", "r", encoding="utf-8") as f:
        with open("data/spark_users_data.json", "w") as fw:
            data = json.load(f)
            for e in data:
                count += 1
                r = requests.get(e['url'], params=param)
                print("count|" + str(count) + "|" + r.url)
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
            if str(tmp[j]).lower().strip() in str(key).lower().strip() or str(key).lower().strip() in str(tmp[j]).lower().strip():
                l1.pop(j)
                l2.pop(j)
    print(l1, l2)
    return l1, l2


if __name__ == '__main__':
    parsing_data()
