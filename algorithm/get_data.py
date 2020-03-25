import numpy


def get_contri_data_from_file(path):
    add_line = []
    del_line = []
    commit = []
    user = []
    age = []
    active_day = []
    with open(path, "r") as f:
        for line in f.readlines():
            info = line.strip().split("\t")
            user.append(info[0])
            commit.append(int(info[1].split('(')[0].strip()))
            add_line.append(int(info[2]))
            del_line.append(int(info[3]))
            age.append(int(info[6].split(' ')[0].strip()))
            active_day.append(int(info[7].strip()))
            # print(info)
    # print(user, commit, add_line, del_line)
    add_line = numpy.asarray(add_line)
    del_line = numpy.asarray(del_line)
    commit = numpy.asarray(commit)
    age = numpy.asarray(age)
    active_day = numpy.asarray(active_day)
    return user, commit, add_line, del_line, age, active_day


def parse_total_any_project_data(
        path="/Users/weizijian/PycharmProjects/ContributerCharacteristics/data/contr_from_gitstats/total_any_project_data.txt"):
    p_name, p_line, p_commit, p_author = [], [], [], []
    with open(path, "r") as f:
        for line in f.readlines():
            s = line.strip().split("||")
            # print(s)
            p_name.append(s[0])
            p_line.append(int(s[2][1:-1].strip().split("|")[0]) + int(s[2][1:-1].strip().split("|")[2]))
            p_commit.append(int(s[3]))
            p_author.append(int(s[5]))
    # return sum(p_line), sum(p_commit), sum(p_author)
    return p_name, p_line, p_commit, p_author


if __name__ == '__main__':
    parse_total_any_project_data()
# total_line, total_commit, total_author = parse_total_any_project_data()
# print(total_commit, total_line, total_author)
