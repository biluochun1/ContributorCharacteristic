from algorithm.analysis import standardize_features, pca_analysis
from algorithm.analysis import spearmanr_rank
from algorithm.calcontri import cal_contri_from_list
from algorithm.get_data import get_contri_data_from_file, parse_total_any_project_data
from algorithm.analysis import linear_regression
import numpy as np

lines = []
commit = []
index = ["commit", "add_line", "del_line", "age", "active_day"]


def cal_all_contri_score():
    p_name, p_line, p_commit, p_author = parse_total_any_project_data()
    with open("all_contri_score.txt", "w") as fw:
        for i in range(len(p_name)):
            path = "/Users/weizijian/PycharmProjects/ContributerCharacteristics/data/contr_from_gitstats/" + p_name[
                i] + "_contri.txt"
            user, commit, add_line, del_line, age, active_day = get_contri_data_from_file(
                path=path)
            # print(p_commit[i], p_line[i])
            user_line = np.asarray(add_line) + np.asarray(del_line)
            contris = cal_contri_from_list(total_line=p_line[i], total_commit=p_commit[i],
                                           single_user_line=user_line.tolist(),
                                           single_user_commit=commit)
            context = p_name[i] + "\t" + str(user) + "\t" + str(contris) + "\n"
            fw.write(context)


if __name__ == '__main__':
    cal_all_contri_score()
    # user, commit, add_line, del_line, age, active_day = get_contri_data_from_file(
    #     path="/Users/weizijian/PycharmProjects/ContributerCharacteristics/data/contr_from_gitstats/total_contri.txt")
    # user_line = np.asarray(add_line) + np.asarray(del_line)
    # contris = cal_contri_from_list(total_line=5940625, total_commit=43604,
    #                                     single_user_line=user_line.tolist(),
    #                                     single_user_commit=commit)
    # print(user)
    # print(contris.tolist())
    # print(len(user))
    # pdata = np.asarray(
    #     [commit, add_line, del_line, age, active_day]).transpose()
    # print(grpc_data)
    # standard_data = np.asarray(standardize_features(pdata))
    # standard_data = np.asarray(standard_data)
    # pca_res = pca_analysis(standard_data, 5)
    # pca_res = np.around(np.asarray(pca_res), decimals=3)
    # np.set_printoptions(suppress=True)
    # print(pca_res)
    # c, p = spearmanr_rank(pdata)
    # print(p)
    # print(c)
    # el = []
    # for i in range(5):
    #     for j in range(5):
    #         el.append([i, j, list(c)[i][j]])
    # print(el)
    # for i in range(1, 6):
    #     sumarry = linear_regression(x=standard_data[:, i], y=standard_data[:, 0])
    #     print("single_regression|" + str(i))
    #     print(sumarry)
    # print(standard_data)
    # print(standard_data.T[np.arange(1, 5)])
    # x = standard_data.T[np.arange(0, 6)].T
    # y = standard_data.T[6]
    # print(x.shape, y.shape)
    # print(y)
    # sumarry = linear_regression(x=x, y=y)

    # y = np.arange(1, 11)
    # x = np.array([[5, 10], [10, 5], [5, 15],
    #               [15, 20], [20, 25], [25, 30], [30, 35],
    #               [35, 5], [5, 10], [10, 15]])
    # print(x.shape,y.shape)
    # sumarry = linear_regression(x=x, y=y)
    # print("line_regression|")
    # print(sumarry)
