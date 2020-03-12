from algorithm.analysis import standardize_features, pca_analysis
from algorithm.analysis import spearmanr_rank
from algorithm.calcontri import cal_contri_from_list
from algorithm.get_data import get_contri_data_from_file
from algorithm.analysis import linear_regression
import numpy as np

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
    grpc_user_line = np.asarray(grpc_add_line) + np.asarray(grpc_del_line)
    grpc_contris = cal_contri_from_list(total_line=5940625, total_commit=43604,
                                        single_user_line=grpc_user_line.tolist(),
                                        single_user_commit=grpc_commit)
    # print(grpc_user)
    # print(grpc_contris.tolist())
    grpc_data = np.asarray(
        [grpc_commit, grpc_add_line, grpc_del_line, grpc_age, grpc_active_day, grpc_tag_count,
         grpc_contris]).transpose()
    # print(grpc_data)
    standard_data = standardize_features(grpc_data)
    # standard_data = np.asarray(standard_data)
    # pca_res = pca_analysis(standard_data, 6)
    # pca_res = np.around(np.asarray(pca_res), decimals=3)
    np.set_printoptions(suppress=True)
    # print(pca_res)
    # c, p = spearmanr_rank(grpc_data)
    # print(p)
    # print(c)
    # for i in range(1, 6):
    #     sumarry = linear_regression(x=standard_data[:, i], y=standard_data[:, 0])
    #     print("single_regression|" + str(i))
    #     print(sumarry)
    # print(standard_data)
    # print(standard_data.T[np.arange(1, 5)])
    x = standard_data.T[np.arange(0, 6)].T
    y = standard_data.T[6]
    print(x.shape, y.shape)
    print(y)
    sumarry = linear_regression(x=x, y=y)

    # y = np.arange(1, 11)
    # x = np.array([[5, 10], [10, 5], [5, 15],
    #               [15, 20], [20, 25], [25, 30], [30, 35],
    #               [35, 5], [5, 10], [10, 15]])
    # print(x.shape,y.shape)
    # sumarry = linear_regression(x=x, y=y)
    print("line_regression|")
    print(sumarry)
