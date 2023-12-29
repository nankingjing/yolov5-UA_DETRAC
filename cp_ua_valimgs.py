image_set = 'val'
import os, shutil
image_paths = open('/data/hyl/guangxizhongqi/UA_DETRAC/data/%s.txt' % (image_set)).read().strip().split()
dst_root_path = "/data/hyl/guangxizhongqi/UA_DETRAC/data/infer_img/ua_val/"
# print(image_paths)
for image_path in image_paths:
  newfile_path = os.path.join(dst_root_path, image_path.split('/')[-1])
  print(newfile_path)
  shutil.copyfile(image_path, newfile_path)