from github import github

username = "823510561@qq.com"
password = "823510561qq"


def run():
    g = github.Github(username=username, password=password)
    r = g.users.getUser()
    print(str(r))


if __name__ == '__main__':
    run()
