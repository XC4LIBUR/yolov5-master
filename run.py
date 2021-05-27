import argparse
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path, save_one_box
import torch
import torch.backends.cudnn as cudnn
from detect import detect


if __name__ == '__main__':
    
    argu = {"agnostic_nms":False, 'augment':False, 'classes':None, 'conf_thres':0.4, 'device':'', 'exist_ok':False, 
            'hide_conf':False, 'hide_labels':False, 'img_size':640, 'iou_thres':0.45, 'line_thickness':3, 'name':'exp', 
                'nosave':False, 'project':'runs/detect', 'save_conf':False, 'save_crop':True, 'save_txt':False, 'source':'images', 
                    'update':False, 'view_img':False, 'weights':['best2.pt']}

    opt=argparse.Namespace(**argu)
    print(opt)
    check_requirements(exclude=('tensorboard', 'pycocotools', 'thop'))

    with torch.no_grad():
        if opt.update:  # update all models (to fix SourceChangeWarning)
            for opt.weights in ['yolov5s.pt', 'yolov5m.pt', 'yolov5l.pt', 'yolov5x.pt']:
                detect(opt=opt)
                strip_optimizer(opt.weights)
        else:
            detect(opt=opt)