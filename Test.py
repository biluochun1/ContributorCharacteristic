from github import github
import json

username = "823510561@qq.com"
password = "823510561qq"


def str2json(s):
    return json.loads(s.decode("utf-8"), encoding="utf-8")


def run():
    g = github.Github(username=username, password=password)
    # _, r = g.users.getUser()
    _, cs = g.repos.listContributors(user="apache", repo="dubbo")
    # user_dict = json.loads(r["body"].decode("utf-8"), encoding="utf-8")
    # print(user_dict["login"])
    for e in cs:
        print(e["login"])


if __name__ == '__main__':
    run()
