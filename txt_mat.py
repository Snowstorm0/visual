import os
import xlwt
import scipy.io

root_path = "/home/xulong/snowstorm/0result/OTB/"
mat_old_path = root_path + '0other_mat/SiamRPN++/'

txt_path = root_path + 'txt_from_SiamRPN++_ECO_anti_all/'
mat_new_path = root_path + 'mat_from_SiamRPN++_ECO_anti_all/'

seq_num = 0

image_names = os.listdir(txt_path) # 获取所有序列名称
image_names.sort() # 按名称排序

for image_name_txt in image_names:
    image_name = image_name_txt[:-4]
    image_name_small = image_name[0:1].lower() + image_name[1:] # 首字母小写

    data = scipy.io.loadmat(mat_old_path + image_name_small + '_SiamRPN++.mat')  # read mat

    txt_result_name = txt_path + image_name + ".txt"
    fopen_result = open(txt_result_name, 'r')
    lines_result = fopen_result.readlines()
    file = xlwt.Workbook(encoding='utf-8', style_compression=0)  # read txt

    # print("data.keys():", data.keys())  # 查看mat文件中的所有变量

    results = data['results']
    # print("results:", results)
    # print("results[0][0][0][0][0]:", results[0][0][0][0][0])

    # write result
    i = 0
    for line in lines_result:

        line = line.strip('\n')
        line = line.split(',')
        # print("line:", line)

        x = float(line[0])
        y = float(line[1])
        w = float(line[2])
        h = float(line[3])
        # print("type_result_x", type(x))

        # for j in range(0, 12):
        for j in range(0, 1):  # OPE
            # results[0][j][0][0][1][i] = [x, y, w, h]  # cv13
            # results[0][j][0][0][5][i] = [x, y, w, h] # pami15
            results[0][j][0][0][0][i] = [x, y, w, h] # pami15
        # print("type_result:", type(results[0][0][0][0][1][0][0]))

        i = i + 1  # 行

    if not os.path.isdir(mat_new_path):
        os.makedirs(mat_new_path)

    scipy.io.savemat(mat_new_path + image_name_small + '_SiamGAN.mat', {'results': results})  # 写入mat文件
    seq_num = seq_num + 1
    print("Save dataset",seq_num, ":", image_name + "_SiamGAN.mat successfully!")
    # # write gt
    # i = 0
    # for line in lines_gt:
    #
    #     line = line.strip('\n')
    #     line = line.split(',')
    #     # print("line:", line)
    #
    #     x = float(line[0])
    #     y = float(line[1])
    #     w = float(line[2])
    #     h = float(line[3])
    #     print("type_gt_x", type(x))
    #
    #     for j in range(0, 12):
    #         results[0][j][0][0][6][i] = [x, y, w, h] # cv13
    #     print("type_gt:", type(results[0][0][0][0][6][0][0]))
    #
    #     i = i + 1  # 行
    #
    # scipy.io.savemat(root_path + "OTB50_mat_1/"  + image_name_small + '_SiG.mat',{ 'results':results}) # 写入mat文件



