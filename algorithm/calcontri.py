import numpy as np


def cal_contri_from_list(total_line: int, single_user_line: list, total_commit: int, single_user_commit: list):
    sl = np.asarray(single_user_line)
    sc = np.asarray(single_user_commit)
    contri = sl / total_line + sc / total_commit
    contri = np.around(contri, decimals=4)
    return contri


