# FDDB-Create-Format-Annotations

Most face detection repositories only support [COCO](https://cocodataset.org/) format and [Widerface](http://shuoyang1213.me/WIDERFACE/) format annotations. However. original [FDDB](http://vis-www.cs.umass.edu/fddb/) dataset does not provide such annotations. This project helps create COCO format and Widerface format annotation files for FDDB.



## Use Annotations

We provide annotation files in COCO and Widerface format for 10-fold cross validation. You can find them in `annotations/COCO/` and `annotations/Widerface/` . Since there is no key point ground truth in FDDB dataset, we simply fake key points.

COCO format example:

```json
{"info": 
 	{"description": "FDDB in COCO format.", 
     "url": "", 
     "version": "1.1", 
     "contributor": "SSRSGJYD", 
     "date_created": "2020-11-15"}, 
 "images": [
     {"file_name": "2002/08/11/big/img_591.jpg", 
      "coco_url": "local", 
      "height": 431, 
      "width": 450, 
      "flickr_url": "local", 
      "id": 1}, 
     ...], 
 "annotations": [
     {"segmentation": [], 
 	  "num_keypoints": 5, 
 	  "keypoints": [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1], 
 	  "iscrowd": 0, 
 	  "area": 43139, 
 	  "image_id": 1, 
 	  "bbox": [180, 41, 179, 241],
      "category_id": 1, 
      "id": 1}, 
	...]
}
```

Widerface format example:

```txt
# 2002/08/11/big/img_591.jpg
180 41 179 241 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```



## Create Annotations By Yourself

Our code works in Python 3.x environments. Install requirements by:

```python
pip3 install -r requirements.txt
```

Download FDDB dataset from [here](http://tamaraberg.com/faceDataset/originalPics.tar.gz) and decompress the two folders into `/fddb/images/` .

To create COCO format annotations:

```python
python fddb2coco.py
```

To create Widerface format annotations:

```python
python fddb2txt.py
```



## Citation

```bibtex
@TechReport{fddbTech,
  author = {Vidit Jain and Erik Learned-Miller},
  title =  {FDDB: A Benchmark for Face Detection in Unconstrained Settings},
  institution =  {University of Massachusetts, Amherst},
  year = {2010},
  number = {UM-CS-2010-009}
  }
```

