# coding=utf-8
import copy
import cv2
import json
import os
import pickle


def create_txt(gt, event_list, split, output_file):
    f = open(output_file, 'w')
    for event in event_list:
        for k, v in gt[int(event)].items():
            imagepath = k.replace('_', '/', 4) + '.jpg'
            f.write('# '+imagepath+'\n')
            for i in range(len(v)):
                x1, y1, wid, hei = int(v[i][0]), int(v[i][1]), int(v[i][2]-v[i][0]), int(v[i][3]-v[i][1])
                f.write('{} {} {} {} 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n'.format(x1,y1,wid,hei))
                
    f.close()


if __name__ == "__main__":
    label_dir = './fddb/'
    image_root = './fddb/images/'
    output_dir = './annotations/Widerface/'

    with open(os.path.join(label_dir, 'gt_box.cache'), 'rb') as f:
        gt = pickle.load(f)

    for i in range(1,11):
        event_list = ['{:02d}'.format(j) for j in range(1,i)] + ['{:02d}'.format(j) for j in range(i+1,11)]
        create_txt(gt, event_list, 'train', os.path.join(output_dir, 'train_fddb_{}.txt'.format(i)))
        create_txt(gt, ['{:02d}'.format(i)], 'val', os.path.join(output_dir, 'val_fddb_{}.txt'.format(i)))
    
