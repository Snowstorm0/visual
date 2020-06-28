# coding=utf-8
import os
import cv2
import imageio
import argparse
from PIL import Image
import numpy as np

# root_path = "/home/xulong/snowstorm/0result/OTB/"
# picture_path = root_path + "0other_picture/SiamRPN++/"
# gif_path = root_path + "0other_gif/SiamRPN++/"
# vedio_path = root_path + "0other_vedio/SiamRPN++/"

root_path = "/home/xulong/snowstorm/0Dataset/MOT/"
picture_path = root_path
gif_path = root_path
vedio_path = root_path + "vedio"

seq_num = 0

images = os.listdir(picture_path) # 获取所有序列名称
images.sort() # 按名称排序
# print("images:", images)

for image_name in images:
    img_seq_path = picture_path + image_name +"/"
    video_name = image_name + '.mp4'
    gif_name = image_name + '.gif'
    video_seq_path = os.path.join(vedio_path, video_name)
    gif_seq_path = os.path.join(gif_path, gif_name)
    # if not os.path.isdir(vedio_path):
    #     os.makedirs(vedio_path)
    # if not os.path.isdir(gif_path):
    #     os.makedirs(gif_path)

    fps = 15   # fps: 帧率
    duration = 1 / fps # 每一帧时间
    seq_num = seq_num + 1 # 序列号

    # ************************* 生成 mp4 *************************
    # fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    for single_image_name in os.listdir(img_seq_path):
        single_img_path = os.path.join(img_seq_path, single_image_name)
        break
    im = Image.open(single_img_path)
    # print("im.size:", im.size)
    vw = cv2.VideoWriter(video_seq_path, fourcc, fps, im.size)
    # vw = cv2.VideoWriter(path, 0x00000021, fps, im.size)


    filenames = os.listdir(img_seq_path)  # 读取单张图片名
    filenames.sort(key=lambda x: int(x[:-4]))  # 排序

    for single_image_name in filenames:
        frame = cv2.imread(img_seq_path + '/' + single_image_name)
        vw.write(frame)

    print("Save vedio",seq_num, ":", image_name, "successfully!")



    # # ************************* 生成 gif *************************
    # frames = []
    # filenames = os.listdir(img_seq_path)
    # filenames.sort(key=lambda x: int(x[:-4]))  # 排序
    # for single_image_name in filenames:
    #     # if (len(single_image_name)) == 12: # VOT
    #     if (len(single_image_name)) == 8: # OTB
    #         print('single_image_name:',single_image_name)
    #         frames.append(imageio.imread(img_seq_path + '/' + single_image_name))
    #     else:
    #         continue
    # imageio.mimsave(gif_seq_path, frames, 'GIF', duration = duration)
    # print("Save gif", seq_num, ":", image_name, "successfully!")



