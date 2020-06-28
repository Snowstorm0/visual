import cv2
import os
import numpy as np
import argparse
import math
import csv



root_path = "/home/xulong/snowstorm/0result/OTB/"
data_path = "/home/xulong/snowstorm/0Dataset/OTB100/"
# txt_path = root_path + "0other_txt/SiamRPN++/"
# img_result_path = root_path + "0other_picture/SiamRPN++/"
txt_path = root_path + "OTB100_txt_s/"
img_result_path = root_path + "OTB100_img_s/"

seq_num = 0

image_names = os.listdir(txt_path) # 获取所有序列名称
image_names.sort() # 按名称排序


for image_name_txt in image_names:
    # print("image_name_txt:", image_name_txt)
    image_name = image_name_txt[:-4]
    img_path = data_path + image_name + "/img/"

    list0 = []
    for files in os.walk(img_path): # 读取所有信息
        list0.append(files)

    img_list = []
    for ii in list0[0][2]: # 读取当前序列内所有图片的名称
        img_list.append(ii)

    list_img_name = np.array(img_list)
    list_img_name.sort() # 对序列内的图片名进行排序
    # print(list_img_name)

    # csv_name = image_name + '.csv'
    txt_name = image_name + '.txt'
    txt_obj = os.path.join(txt_path, txt_name)
    txt_file = csv.reader(open(txt_obj))  # 读取该序列对应的txt

    list2 = []
    for i in txt_file: # 读取 bbox
        list2.append(i)
    list3 = np.array(list2) # bbox
    list4 = []
    list_temp = []
    for j in list3:
        list_temp = np.array([0.0 if y == '' else float(y) for y in j])
        list4.append(list_temp)
    list5 = np.array(list4) # bbox
    list_temp1 = []
    list_temp2 = []
    for k in list5:
        list_temp1 = np.array([int(z) for z in k])
        list_temp2.append(list_temp1)
    list_rect = np.array(list_temp2)  # 得到 int 形式的 bbox


    img_num = len(list_rect) - 1
    for num in range(0, img_num):
        if list_rect[num][0] > 2:
            img_file_name = img_path + str(list_img_name[num])
            src = cv2.imread(img_file_name)
            # cv2.imshow('aa',src)
            # cv2.waitKey(0)

            if len(list_rect[num]) == 4:
                x1 = list_rect[num][0]
                y1 = list_rect[num][1]
                w = list_rect[num][2]
                h = list_rect[num][3]
                x2 = x1 + w
                y2 = y1 + h
                cv2.rectangle(src, (x1, y1), (x2, y2), (0, 0, 255), 3)
                # print("number:", num, "  len:", len(list_rect[num]), "  bbox:", (x1, y1), (x2, y2))

            elif len(list_rect[num]) == 8:
                x1 = min(list_rect[num][0], list_rect[num][2], list_rect[num][4], list_rect[num][6])
                x2 = max(list_rect[num][0], list_rect[num][2], list_rect[num][4], list_rect[num][6])
                y1 = min(list_rect[num][1], list_rect[num][3], list_rect[num][5], list_rect[num][7])
                y2 = max(list_rect[num][1], list_rect[num][3], list_rect[num][5], list_rect[num][7])
                w = x2 - x1
                h = y2 - y1
                cv2.rectangle(src, (x1, y1), (x2, y2), (0, 0, 255), 3)
                # print("number:", num, "  len:", len(list_rect[num]), "  bbox:", (x1, y1), (x2, y2))

            else:
                print("data error!")

            # cv2.imshow('aa',src)
            # cv2.waitKey(0)

            save_name = image_name + '/'
            save_path = os.path.join(img_result_path, save_name) # 保存序列
            save_file_name = save_path + str(list_img_name[num]) # 保存序列内每张图
            if not os.path.isdir(save_path):
                os.makedirs(save_path)
            cv2.imwrite(save_file_name, src)

    seq_num = seq_num + 1
    print("Save image",seq_num, ":", image_name, " successfully!")

