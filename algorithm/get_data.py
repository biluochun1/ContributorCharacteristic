import numpy


def get_contri_data_from_file(path):
    add_line = []
    del_line = []
    commit = []
    user = []
    age = []
    active_day = []
    tag_count = []
    with open(path, "r") as f:
        for line in f.readlines():
            info = line.strip().split("\t")
            user.append(info[0])
            commit.append(int(info[1].split('(')[0].strip()))
            add_line.append(int(info[2]))
            del_line.append(int(info[3]))
            age.append(int(info[6].split(' ')[0].strip()))
            active_day.append(int(info[7].strip()))
            tag_count.append(int(info[8].strip()))
            # print(info)
    # print(user, commit, add_line, del_line)
    add_line = numpy.asarray(add_line)
    del_line = numpy.asarray(del_line)
    commit = numpy.asarray(commit)
    age = numpy.asarray(age)
    active_day = numpy.asarray(active_day)
    tag_count = numpy.asarray(tag_count)
    return user, commit, add_line, del_line, age, active_day, tag_count
