import numpy as np


def cal_contri_from_list(total_line: int, single_user_line: list, total_commit: int, single_user_commit: list):
    sl = np.asarray(single_user_line)
    sc = np.asarray(single_user_commit)
    contri = sl / total_line + sc / total_commit
    contri = np.around(contri, decimals=4)
    return contri


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
    return user, commit, add_line, del_line, age, active_day, tag_count


if __name__ == '__main__':
    # grpc_user_add_line = [1480450, 308815, 171412, 76855, 251563, 129273, 217183, 93341, 94978, 40816, 75091, 45901,
    #                       51898, 26411, 16604, 54211, 16880, 30114, 63621, 12344]
    # grpc_user_del_line = [1245505, 442010, 94628, 53173, 182052, 92913, 130330, 146583, 16758, 39975, 46649, 26273,
    #                       35921, 11095, 19752, 34179, 13525, 14574, 69933, 6841]
    # grpc_user_commit = [8381, 4800, 1806, 1636, 1548, 1389, 1283, 1109, 993, 950, 828, 813, 813, 805, 776, 677, 655,
    #                     647, 632, 616]
    # grpc_user_line = np.asarray(grpc_user_add_line) + np.asarray(grpc_user_del_line)
    # grpc_contris = cal_contri_from_list(total_line=5940625, total_commit=43604,
    #                                     single_user_line=grpc_user_line.tolist(),
    #                                     single_user_commit=grpc_user_commit)
    # print(grpc_contris)
    grpc_user, grpc_commit, grpc_add_line, grpc_del_line, grpc_age, grpc_active_day, grpc_tag_count = get_contri_data_from_file(
        path="../data/grpc_contr.txt")
    # grpc_user_line = np.asarray(grpc_add_line) + np.asarray(grpc_del_line)
    # grpc_contris = cal_contri_from_list(total_line=5940625, total_commit=43604,
    #                                     single_user_line=grpc_user_line.tolist(),
    #                                     single_user_commit=grpc_commit)
    # print(grpc_user)
    # print(grpc_contris.tolist())
    print(grpc_age, grpc_active_day)
