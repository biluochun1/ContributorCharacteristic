from github import github
import json

username = "823510561@qq.com"
password = "823510561qq"


def str2json(s):
    return json.loads(s.decode("utf-8"), encoding="utf-8")


def run():
    g = github.Github(username=username, password=password)
    # _, r = g.users.getUser()
    # user_dict = json.loads(r["body"].decode("utf-8"), encoding="utf-8")
    # print(user_dict["login"])
    resp = g.events.listRepoEvents(repo="grpc",user="Craig Tiller")
    print(resp)



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

if __name__ == '__main__':
    run()
    # parse_4days_log()
