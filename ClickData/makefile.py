# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @File         :makefile.py
# @Author       :sunshine
# @Date         :2022/5/26 15:04 
# @python       : 3.9
# @Description  :
"""
import os
def make_data_dir_yaml(yaml_name, data_dir_name, nums, class_names):
    # 生成数据集必要图片和标签文件夹
    for dirs in ['train/images', 'train/labels', 'valid/images', 'valid/labels']:
        try:
            os.makedirs(dirs)
        except FileExistsError:
            print(f'{dirs} 目录已存在')
    # 生成数据集配置.yaml
    with open(yaml_name, "w", encoding='utf-8') as f:
        f.write(f"train: ./{data_dir_name}/train/images\n")
        f.write(f"val: ./{data_dir_name}/valid/images\n")
        f.write("\n")
        f.write(f"nc: {nums}\n")
        f.write(f"names: {class_names}\n")


make_data_dir_yaml('test.yaml', 'ClickData', 3, ['dog', 'cat', 'pig'])
