# -*- coding: utf-8 -*-
'''
palette.py
==============================
test_segmentation.py でクラスマップに塗る色を定義する。
'''


# クラス毎に色を指定する。色の順番は BGR。
sky          = [128, 128, 128]
building     = [128,   0,   0]
pole         = [192, 192, 128]
#road_marking = [255,  69,   0]
road         = [128,  64, 128]
pavement     = [ 60,  40, 222]
tree         = [128, 128,   0]
sign_symbol  = [192, 128, 128]
fence        = [ 64,  64, 128]
car          = [ 64,   0, 128]
pedestrian   = [ 64,  64,   0]
bicyclist    = [  0, 128, 192]
unlabeled    = [  0,   0,   0]


# 結果を可視化するときに使う色のパレット。
# test_segmentation.py で読み込む。
palette = [
    sky,
    building,
    pole,
    road,
    pavement,
    tree,
    sign_symbol,
    fence,
    car,
    pedestrian,
    bicyclist,
    unlabeled
]