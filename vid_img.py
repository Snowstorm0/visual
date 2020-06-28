import cv2
import os


def save_img():
    # video_path = r'E:\\0OneDrive\\OneDrive\\CNN\\result\\1\\'
    video_path = r'/home/xulong/snowstorm/0result/0other/MOT_result_vedio/'
    picture_path = r'/home/xulong/snowstorm/0result/0other/MOT_result_img/'
    videos = os.listdir(video_path)
    videos.sort()  # 按名称排序
    seq_num = 0

    for video_name in videos:
        # print("video_name:", video_name)
        file_name = video_name.split('.')[0]
        print("file_name:", file_name)
        folder_name = video_path + file_name
        os.makedirs(folder_name,exist_ok=True)
        vc = cv2.VideoCapture(video_path + video_name) #读入视频文件
        c=0
        rval=vc.isOpened()
        seq_num = seq_num + 1  # 序列号

        while rval:   #循环读取视频帧
            c = c + 1
            rval, frame = vc.read()
            # pic_path = folder_name+'\\'
            pic_path = picture_path + file_name + '/'
            if not os.path.isdir(pic_path):
                os.makedirs(pic_path)
            # print("pic_path:", pic_path)
            if rval:
                # print(len(str(c)))
                if len(str(c)) == 1:
                    # cv2.imwrite(pic_path + file_name + '_000' + str(c) + '.jpg', frame)
                    # 存储为图像,保存名为 文件夹名_数字（第几个文件）.jpg
                    cv2.imwrite(pic_path + '0000' + str(c) + '.jpg', frame)
                elif len(str(c)) == 2:
                    cv2.imwrite(pic_path + '000' + str(c) + '.jpg', frame)
                elif len(str(c)) == 3:
                    cv2.imwrite(pic_path + '00' + str(c) + '.jpg', frame)
                elif len(str(c)) == 4:
                    cv2.imwrite(pic_path + '0' + str(c) + '.jpg', frame)
                else:
                    cv2.imwrite(pic_path + str(c) + '.jpg', frame)

                cv2.waitKey(5)
            else:
                break
        vc.release()
        print("Save vedio", seq_num, ":", video_name, "successfully!")

save_img()

