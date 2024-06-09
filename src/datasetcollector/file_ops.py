import shutil
import os 

def copy_folder(src, dst):
    try:
        img_ids = []
        for img in os.listdir(src):
            img_ids.append(f"{src}/{img}".split('.')[0].split('/')[1].split('_')[-1])
            shutil.copy(f"{src}/{img}", dst)
        return max(int(img_id) for img_id in img_ids) + 1
    except:
        return 0 

def delete_folder(path):
    try:
        for img in os.listdir(path):
            os.remove(f"{path}/{img}")
        os.rmdir(path) 
    except:
        pass 