# coding=utf-8
import copy
import cv2
import json
import os
import pickle

dataset = { "info": {
            "description": "FDDB in COCO format.",
            "url": "",
            "version": "1.1",
            "contributor": "SSRSGJYD",
            "date_created": "2020-11-15"},
            "images": [],
            "annotations": [],
            "categories": [{'id': 1, 'name': 'face'}],
}

def create_coco(gt, event_list, split, output_file):
    img_id=1
    anno_id=1
    cur_dataset = copy.deepcopy(dataset)
    for event in event_list:
        for k, v in gt[int(event)].items():
            imagepath = k.replace('_', '/', 4) + '.jpg'
            im = os.path.join(image_root, imagepath)
            im = cv2.imread(im)
            height, width, channels = im.shape
            cur_dataset["images"].append({"file_name": imagepath, "coco_url": "local", "height": height, "width": width, "flickr_url": "local", "id": img_id})

            for i in range(len(v)):
                x1, y1, wid, hei = int(v[i][0]), int(v[i][1]), int(v[i][2]-v[i][0]), int(v[i][3]-v[i][1])
                cur_dataset["annotations"].append({
                    "segmentation": [],
                    "num_keypoints": 5,
                    "keypoints": [0,0,1,0,0,1,0,0,1,0,0,1,0,0,1], # fake keypoints
                    "iscrowd": 0,
                    "area": wid * hei,
                    "image_id": img_id,
                    "bbox": [x1, y1, wid, hei],
                    "category_id": 1,
                    "id": anno_id})
                anno_id = anno_id + 1
            img_id += 1

    with open(output_file, 'w') as f:
        json.dump(cur_dataset, f)


if __name__ == "__main__":
    label_dir = './fddb/'
    image_root = './fddb/images/'
    output_dir = './annotations/COCO/'

    with open(os.path.join(label_dir, 'gt_box.cache'), 'rb') as f:
        gt = pickle.load(f)

    for i in range(1,11):
        event_list = ['{:02d}'.format(j) for j in range(1,i)] + ['{:02d}'.format(j) for j in range(i+1,11)]
        create_coco(gt, event_list, 'train', os.path.join(output_dir, 'train_fddb_{}.json'.format(i)))
        create_coco(gt, ['{:02d}'.format(i)], 'val', os.path.join(output_dir, 'val_fddb_{}.json'.format(i)))
        
