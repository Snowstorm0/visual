import os
import xlwt
import scipy.io
import h5py
import numpy as np

root_path = "/home/xulong/snowstorm/0result/OTB/"
mat_path = root_path + '0other_mat/ECO/'
txt_path = root_path + '0other_txt/ECO/'

seq_num = 0

image_names = os.listdir(root_path + "0list/") # 获取所有序列名称
image_names.sort() # 按名称排序

for image_name_txt in image_names:
    image_name = image_name_txt[:-4]
    image_name_small = image_name[0:1].lower() + image_name[1:] # 首字母小写

    if not os.path.isdir(txt_path):
        os.makedirs(txt_path)

    txt_name = txt_path + image_name + ".txt"
    file_write = open(txt_name, 'w') # 以写的方式打开txt，如果文件不存在，就会自动创建

    # data = scipy.io.loadmat(mat_path + "OPE_" + image_name + '.mat')  # 用 scipy 读 mat
    # mat = data['results']
    # bbox = mat[0][0][0][0][0]

    dict_data = h5py.File(mat_path + image_name + "_ECO" +'.mat', 'r') # 用 h5py 读 mat
    # def pprint(name):
    #     print(name)
    # dict_data.visit(pprint) # 获取索引目录
    a = np.array(dict_data["#refs#/b/res"][:])
    bbox = a.T

    for i in range(len(bbox)):
        file_write.write(str(bbox[i][0]))
        file_write.write(str(","))
        file_write.write(str(bbox[i][1]))
        file_write.write(str(","))
        file_write.write(str(bbox[i][2]))
        file_write.write(str(","))
        file_write.write(str(bbox[i][3]))
        file_write.write('\n')

    file_write.close()

    seq_num = seq_num + 1
    print("Save dataset", seq_num, ":", image_name + ".txt successfully!")


