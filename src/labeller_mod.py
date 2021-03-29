# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'label_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import cv2
import copy
import json
import os
import numpy as np
np.set_printoptions(precision=1)
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.utils import draw_3D_labels
from GUI.utils import get_annotations


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.sync_offsets = [0,0,0,0]
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1334, 931)

        image_list_file = open("data/wibam/image_sets/val.txt", "r")
        self.image_list = image_list_file.read().split("\n")
        image_list_file.close()


        self.image_dir = "data/wibam/frames/"
        self.hand_labels = "data/wibam/annotations/hand_labels/"
        self.auto_labels = "data/wibam/annotations/wibam_val.json"
        self.image_extension = ".jpg"
        self.image_idx = 0
        self.image_id = '0'
        self.calib = None
        self.current_images = []
        self.drawnon_images = []
        self.cams = [0,1,2,3]
        
        self.current_objects = []
        self.num_objects = 0

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(250, 90, 1024, 576))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("../../data/wibam/frames/0/0.jpg"))
        self.image.setScaledContents(True)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.xSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.xSpinBox.setGeometry(QtCore.QRect(550, 740, 71, 91))
        self.xSpinBox.setMinimum(-100.0)
        self.xSpinBox.setSingleStep(0.1)
        self.xSpinBox.setProperty("value", 20.0)
        self.xSpinBox.setObjectName("xSpinBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 770, 16, 20))
        self.label_2.setObjectName("label_2")
        self.ySpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.ySpinBox.setGeometry(QtCore.QRect(650, 740, 71, 91))
        self.ySpinBox.setMinimum(-100.0)
        self.ySpinBox.setMaximum(100.0)
        self.ySpinBox.setSingleStep(0.1)
        self.ySpinBox.setProperty("value", 20.0)
        self.ySpinBox.setObjectName("ySpinBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(640, 770, 20, 20))
        self.label_3.setObjectName("label_3")
        self.zSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.zSpinBox.setGeometry(QtCore.QRect(750, 740, 71, 91))
        self.zSpinBox.setMinimum(-2.0)
        self.zSpinBox.setMaximum(2.0)
        self.zSpinBox.setSingleStep(0.1)
        self.zSpinBox.setObjectName("zSpinBox")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(740, 770, 16, 20))
        self.label_4.setObjectName("label_4")
        self.lengthSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lengthSpinBox.setGeometry(QtCore.QRect(960, 740, 71, 91))
        self.lengthSpinBox.setSingleStep(0.1)
        self.lengthSpinBox.setProperty("value", 5.0)
        self.lengthSpinBox.setObjectName("lengthSpinBox")
        self.widthSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.widthSpinBox.setGeometry(QtCore.QRect(1060, 740, 71, 91))
        self.widthSpinBox.setSingleStep(0.1)
        self.widthSpinBox.setProperty("value", 2.5)
        self.widthSpinBox.setObjectName("widthSpinBox")

        self.cam0SpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.cam0SpinBox.setGeometry(QtCore.QRect(10, 330, 48, 26))
        self.cam0SpinBox.setSingleStep(1)
        self.cam0SpinBox.setProperty("value", 0)
        self.cam0SpinBox.setObjectName("cam0SpinBox")
        self.cam0SpinBox.setMinimum(-100)
        self.cam1SpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.cam1SpinBox.setGeometry(QtCore.QRect(70, 330, 48, 26))
        self.cam1SpinBox.setSingleStep(1)
        self.cam1SpinBox.setProperty("value", 0)
        self.cam1SpinBox.setObjectName("cam1SpinBox")
        self.cam1SpinBox.setMinimum(-100)
        self.cam2SpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.cam2SpinBox.setGeometry(QtCore.QRect(130, 330, 48, 26))
        self.cam2SpinBox.setSingleStep(1)
        self.cam2SpinBox.setProperty("value", 0)
        self.cam2SpinBox.setObjectName("cam2SpinBox")
        self.cam2SpinBox.setMinimum(-100)
        self.cam3SpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.cam3SpinBox.setGeometry(QtCore.QRect(190, 330, 48, 26))
        self.cam3SpinBox.setSingleStep(1)
        self.cam3SpinBox.setProperty("value", 0)
        self.cam3SpinBox.setObjectName("cam3SpinBox")
        self.cam3SpinBox.setMinimum(-100)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1140, 770, 16, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1040, 770, 16, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(950, 770, 20, 20))
        self.label_7.setObjectName("label_7")
        self.heightSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.heightSpinBox.setGeometry(QtCore.QRect(1160, 740, 71, 91))
        self.heightSpinBox.setSingleStep(0.1)
        self.heightSpinBox.setProperty("value", 2.5)
        self.heightSpinBox.setObjectName("heightSpinBox")
        self.visibleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.visibleSpinBox.setGeometry(QtCore.QRect(1260, 740, 71, 91))
        self.visibleSpinBox.setSingleStep(0.1)
        self.visibleSpinBox.setProperty("value", 1.)
        self.visibleSpinBox.setObjectName("visibleSpinBox")
        self.visibleSpinBox.setMaximum(1.)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(830, 770, 31, 20))
        self.label_8.setObjectName("label_8")
        self.rotSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.rotSpinBox.setGeometry(QtCore.QRect(850, 740, 71, 91))
        self.rotSpinBox.setMaximum(360.0)
        self.rotSpinBox.setSingleStep(5.0)
        self.rotSpinBox.setObjectName("rotSpinBox")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(540, 700, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")

        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(10, 290, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(940, 700, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(1240, 700, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.objectSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.objectSpinBox.setGeometry(QtCore.QRect(390, 740, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.objectSpinBox.setFont(font)
        self.objectSpinBox.setMaximum(0)
        self.objectSpinBox.setMinimum(0)
        self.objectSpinBox.setObjectName("objectSpinBox")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(390, 720, 101, 17))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(280, 720, 101, 17))
        self.label_12.setObjectName("label_12")
        self.imageSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.imageSpinBox.setGeometry(QtCore.QRect(280, 740, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.imageSpinBox.setFont(font)
        self.imageSpinBox.setMinimum(0)
        self.imageSpinBox.setMaximum(5)
        self.imageSpinBox.setObjectName("imageSpinBox")
        self.addObjectButton = QtWidgets.QPushButton(self.centralwidget)
        self.addObjectButton.setGeometry(QtCore.QRect(390, 690, 89, 25))
        self.addObjectButton.setObjectName("addObjectButton")
        self.nextImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextImageButton.setGeometry(QtCore.QRect(1170, 60, 100, 25))
        self.nextImageButton.setObjectName("nextImageButton")
        self.previousImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.previousImageButton.setGeometry(QtCore.QRect(1060, 60, 100, 25))
        self.previousImageButton.setObjectName("previousImageButton")
        self.saveLabelButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveLabelButton.setGeometry(QtCore.QRect(250, 60, 89, 25))
        self.saveLabelButton.setObjectName("saveLabelButton")
        self.deleteLabelButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteLabelButton.setGeometry(QtCore.QRect(450, 60, 89, 25))
        self.deleteLabelButton.setObjectName("deleteLabelButton")
        self.initLabelButton = QtWidgets.QPushButton(self.centralwidget)
        self.initLabelButton.setGeometry(QtCore.QRect(350, 60, 89, 25))
        self.initLabelButton.setObjectName("initLabelButton")
        self.estimateLabelButton = QtWidgets.QPushButton(self.centralwidget)
        self.estimateLabelButton.setGeometry(QtCore.QRect(350, 30, 89, 25))
        self.estimateLabelButton.setObjectName("estimateLabelButton")
        self.fileNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.fileNameLabel.setGeometry(QtCore.QRect(150, 90, 67, 17))
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.idxLabel = QtWidgets.QLabel(self.centralwidget)
        self.idxLabel.setGeometry(QtCore.QRect(150, 70, 67, 17))
        self.idxLabel.setObjectName("idxLabel")
        self.numObjectsLabel = QtWidgets.QLabel(self.centralwidget)
        self.numObjectsLabel.setGeometry(QtCore.QRect(150, 110, 91, 17))
        self.numObjectsLabel.setObjectName("numObjectsLabel")
        self.cameraNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.cameraNumLabel.setGeometry(QtCore.QRect(150, 130, 91, 17))
        self.cameraNumLabel.setObjectName("cameraNumLabel")
        self.FLpoint = QtWidgets.QLabel(self.centralwidget)
        self.FLpoint.setGeometry(QtCore.QRect(10, 160, 111, 16))
        self.FLpoint.setObjectName("FLpoint")
        self.FRpoint = QtWidgets.QLabel(self.centralwidget)
        self.FRpoint.setGeometry(QtCore.QRect(140, 160, 111, 17))
        self.FRpoint.setObjectName("FRpoint")
        self.RLpoint = QtWidgets.QLabel(self.centralwidget)
        self.RLpoint.setGeometry(QtCore.QRect(10, 230, 111, 17))
        self.RLpoint.setObjectName("RLpoint")
        self.RRpoint = QtWidgets.QLabel(self.centralwidget)
        self.RRpoint.setGeometry(QtCore.QRect(140, 230, 111, 17))
        self.RRpoint.setObjectName("RRpoint")
        self.FRpointGround = QtWidgets.QLabel(self.centralwidget)
        self.FRpointGround.setGeometry(QtCore.QRect(140, 180, 111, 17))
        self.FRpointGround.setObjectName("FRpointGround")
        self.FLpointGround = QtWidgets.QLabel(self.centralwidget)
        self.FLpointGround.setGeometry(QtCore.QRect(10, 180, 111, 16))
        self.FLpointGround.setObjectName("FLpointGround")
        self.RLpointGround = QtWidgets.QLabel(self.centralwidget)
        self.RLpointGround.setGeometry(QtCore.QRect(10, 247, 111, 20))
        self.RLpointGround.setObjectName("RLpointGround")
        self.RRpointGround = QtWidgets.QLabel(self.centralwidget)
        self.RRpointGround.setGeometry(QtCore.QRect(140, 250, 111, 17))
        self.RRpointGround.setObjectName("RRpointGround")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(30, 90, 81, 17))
        self.label_13.setObjectName("label_13")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(30, 70, 81, 17))
        self.label_17.setObjectName("label_17")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 110, 91, 17))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(30, 130, 67, 17))
        self.label_15.setObjectName("label_15")

        self.removeObjectButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeObjectButton.setGeometry(QtCore.QRect(10, 840, 150, 25))
        self.removeObjectButton.setObjectName("removeObjectButton")
        self.removeAllObjectsButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeAllObjectsButton.setGeometry(QtCore.QRect(10, 875, 170, 25))
        self.removeAllObjectsButton.setObjectName("removeObjectButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1334, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.imageSpinBox.valueChanged.connect(self.change_cam)
        self.objectSpinBox.valueChanged.connect(self.update_spin_params)
        self.xSpinBox.valueChanged.connect(self.update_params)
        self.ySpinBox.valueChanged.connect(self.update_params)
        self.zSpinBox.valueChanged.connect(self.update_params)
        self.lengthSpinBox.valueChanged.connect(self.update_params)
        self.widthSpinBox.valueChanged.connect(self.update_params)
        self.heightSpinBox.valueChanged.connect(self.update_params)
        self.rotSpinBox.valueChanged.connect(self.update_params)
        self.visibleSpinBox.valueChanged.connect(self.update_params)
        self.cam0SpinBox.valueChanged.connect(self.sync_image)
        self.cam1SpinBox.valueChanged.connect(self.sync_image)
        self.cam2SpinBox.valueChanged.connect(self.sync_image)
        self.cam3SpinBox.valueChanged.connect(self.sync_image)

        self.spin_boxes = [
            self.xSpinBox, self.ySpinBox, self.zSpinBox,
            self.lengthSpinBox, self.widthSpinBox, self.heightSpinBox,
            self.rotSpinBox
        ]
        
        self.nextImageButton.clicked.connect(self.next_image)
        self.previousImageButton.clicked.connect(self.previous_image)
        self.addObjectButton.clicked.connect(self.create_new_object)
        self.removeObjectButton.clicked.connect(self.remove_current_object)
        self.removeAllObjectsButton.clicked.connect(self.remove_all_objects)
        self.saveLabelButton.clicked.connect(self.save_labels)
        self.initLabelButton.clicked.connect(self.init_labels)
        self.estimateLabelButton.clicked.connect(self.estimate_labels)
        self.deleteLabelButton.clicked.connect(self.delete_labels)

        self.create_new_object()
        self.next_image()
        self.update()
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "X"))
        self.label_3.setText(_translate("MainWindow", "Y"))
        self.label_4.setText(_translate("MainWindow", "Z"))
        self.label_5.setText(_translate("MainWindow", "H"))
        self.label_6.setText(_translate("MainWindow", "W"))
        self.label_7.setText(_translate("MainWindow", "L"))
        self.label_8.setText(_translate("MainWindow", "rot"))
        self.label_9.setText(_translate("MainWindow", "Position"))
        self.label_10.setText(_translate("MainWindow", "Size"))
        self.label_16.setText(_translate("MainWindow", "Visible"))
        self.label_11.setText(_translate("MainWindow", "Object select"))
        self.label_12.setText(_translate("MainWindow", "View select"))
        self.addObjectButton.setText(_translate("MainWindow", "Add object"))
        self.nextImageButton.setText(_translate("MainWindow", "Next Image"))
        self.previousImageButton.setText(_translate("MainWindow", "Previous Image"))
        self.saveLabelButton.setText(_translate("MainWindow", "Save label"))
        self.deleteLabelButton.setText(_translate("MainWindow", "Delete label"))
        self.initLabelButton.setText(_translate("MainWindow", "Initialise label"))
        self.estimateLabelButton.setText(_translate("MainWindow", "Estimate label"))
        self.fileNameLabel.setText(_translate("MainWindow", "FileName"))
        self.idxLabel.setText(_translate("MainWindow", "IndexName"))
        self.numObjectsLabel.setText(_translate("MainWindow", "NumObjects"))
        self.cameraNumLabel.setText(_translate("MainWindow", "CamLabel"))
        self.FLpoint.setText(_translate("MainWindow", "FL coord"))
        self.FRpoint.setText(_translate("MainWindow", "FR coord"))
        self.RLpoint.setText(_translate("MainWindow", "RL coord"))
        self.RRpoint.setText(_translate("MainWindow", "RR coord"))
        self.FRpointGround.setText(_translate("MainWindow", "FR coord"))
        self.FLpointGround.setText(_translate("MainWindow", "FL coord"))
        self.RLpointGround.setText(_translate("MainWindow", "RL coord"))
        self.RRpointGround.setText(_translate("MainWindow", "RR coord"))
        self.label_13.setText(_translate("MainWindow", "File name:"))
        self.label_17.setText(_translate("MainWindow", "Idx #: "))
        self.label_14.setText(_translate("MainWindow", "Num objects:"))
        self.label_15.setText(_translate("MainWindow", "Camera:"))
        self.label_18.setText(_translate("MainWindow", "Sync offsets"))
        self.removeObjectButton.setText(_translate("MainWindow", "Remove this object"))
        self.removeAllObjectsButton.setText(_translate("MainWindow", "Remove all objects"))

    def update(self):
        self.update_current_images()
        self.draw_labels()
        self.change_cam()
        self.objectSpinBox.setMaximum(len(self.current_objects)-1)
        if len(self.current_objects) > 0:
            self.objectSpinBox.setMinimum(0)

    def set_image(self, opencv_image):
        h, w, c = opencv_image.shape
        bytesPerLine = 3 * w
        QImg = QtGui.QImage(opencv_image.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
        self.image.setPixmap(QtGui.QPixmap.fromImage(QImg))

    def get_current_object(self):
        for obj in self.current_objects:
            if obj['current']:
                return obj
        return None

    def change_cam(self):
        image_num = self.imageSpinBox.value() 
        image = self.drawnon_images[image_num]
        self.cameraNumLabel.setText(str(self.imageSpinBox.value()))
        self.imageSpinBox.setMaximum(len(self.drawnon_images)-1)
        if image_num < 4 and len(self.current_objects) > 0:
            self.visibleSpinBox.setValue(
                self.get_current_object()['visibility'][image_num]
            )
        else:
            self.visibleSpinBox.setValue(-1)
        self.set_image(image)

    def update_current_images(self):
        self.image_id = self.image_list[self.image_idx]
        self.fileNameLabel.setText(self.image_id)
        self.idxLabel.setText(str(self.image_idx))
        self.current_images = []
        self.drawnon_images = []
        for i in range(len(self.cams)):
            img_id = str(int(self.image_id) + self.sync_offsets[i])
            file_name = self.image_dir + str(self.cams[i]) + "/" + img_id + self.image_extension
            img = cv2.imread(file_name)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.current_images.append(img)
            self.drawnon_images.append(img.copy())
        self.draw_labels()

    def sync_image(self):
        self.sync_offsets[0] = self.cam0SpinBox.value()
        self.sync_offsets[1] = self.cam1SpinBox.value()
        self.sync_offsets[2] = self.cam2SpinBox.value()
        self.sync_offsets[3] = self.cam3SpinBox.value()
        self.update_current_images()
        self.change_cam()
        self.imageSpinBox.setMaximum(len(self.drawnon_images)-1)
        self.draw_labels()

    def next_image(self):
        if self.image_idx < len(self.image_list)-2:
            self.image_idx += 1
        self.update_current_images()
        self.change_cam()
        self.imageSpinBox.setMaximum(len(self.drawnon_images)-1)
        self.load_labels()
        self.sync_image()

    def previous_image(self):
        if self.image_idx > 0:
            self.image_idx -= 1
        
        self.image_id = self.image_list[self.image_idx]
        self.update_current_images()
        self.change_cam()
        self.imageSpinBox.setMaximum(len(self.drawnon_images)-1)
        self.load_labels()

    def create_new_object(self, loc=None):
        object_id = self.num_objects
        object_dict = {}
        object_dict['current'] = True
        object_dict['l'] = 4.78
        object_dict['w'] = 2.1
        object_dict['h'] = 1.86
        if loc is None or loc is False: 
            object_dict['x'] = 20. + random.randint(-10,10)
            object_dict['y'] = 20. + random.randint(-10,10)
            object_dict['z'] = 0.
        else:
            object_dict['x'] = loc[0]
            object_dict['y'] = loc[1]
            object_dict['z'] = 0.
        object_dict['rot'] = 0. + random.randint(0,360)
        object_dict['visibility'] = [1,1,1,1]
        self.current_objects.append(object_dict)
        self.num_objects = len(self.current_objects)

        self.objectSpinBox.setMinimum(0)
        self.objectSpinBox.setMaximum(self.num_objects-1)
        self.numObjectsLabel.setText(str(self.num_objects))

        self.update()

    def remove_current_object(self):
        for spin_box in self.spin_boxes:
            spin_box.blockSignals(True)
        if len(self.current_objects) > 0:
            object_id = self.objectSpinBox.value()
            self.current_objects.pop(object_id)
            if len(self.current_objects) == 0:
                self.create_new_object()
            self.num_objects = len(self.current_objects)
            self.objectSpinBox.setMaximum(self.num_objects-1)
            self.numObjectsLabel.setText(str(self.num_objects))
        else:
            self.create_new_object()
        for spin_box in self.spin_boxes:
            spin_box.blockSignals(False)
        self.update_spin_params()

    def remove_all_objects(self):
        for spin_box in self.spin_boxes:
            spin_box.blockSignals(True)
        self.current_objects = []
        self.create_new_object()
        self.num_objects = len(self.current_objects)
        self.objectSpinBox.setMaximum(self.num_objects-1)
        self.numObjectsLabel.setText(str(self.num_objects))
        for spin_box in self.spin_boxes:
            spin_box.blockSignals(False)
        self.update()

    def update_params(self):
        if len(self.current_objects) < 1:
            return
        if len(self.current_objects)-1 < self.objectSpinBox.value():
            self.objectSpinBox.setValue(self.objectSpinBox.value()-1)
        self.objectSpinBox.setMaximum(len(self.current_objects))
        obj = self.current_objects[self.objectSpinBox.value()]
        obj['x'] = self.xSpinBox.value()
        obj['y'] = self.ySpinBox.value()
        obj['z'] = self.zSpinBox.value()
        obj['l'] = self.lengthSpinBox.value()
        obj['w'] = self.widthSpinBox.value()
        obj['h'] = self.heightSpinBox.value()
        obj['rot'] = self.rotSpinBox.value()
        if self.imageSpinBox.value() < 4:
            obj['visibility'][self.imageSpinBox.value()] = \
                self.visibleSpinBox.value() 
        self.draw_labels()
        self.change_cam()

    def update_spin_params(self):
        try:
            obj = self.current_objects[self.objectSpinBox.value()]
        except:
            return
        for spin_box in self.spin_boxes:
            spin_box.blockSignals(True)

        for o in self.current_objects:
            if o is not obj:
                o['current'] = False

        # self.sync_image()

        obj['current'] = True
        self.rotSpinBox.setValue(obj['rot'])
        self.xSpinBox.setValue(obj['x'])
        self.ySpinBox.setValue(obj['y'])
        self.zSpinBox.setValue(obj['z'])
        self.lengthSpinBox.setValue(obj['l'])
        self.widthSpinBox.setValue(obj['w'])
        self.heightSpinBox.setValue(obj['h'])
        self.cam0SpinBox.setValue(self.sync_offsets[0])
        self.cam1SpinBox.setValue(self.sync_offsets[1])
        self.cam2SpinBox.setValue(self.sync_offsets[2])
        self.cam3SpinBox.setValue(self.sync_offsets[3])

        self.update()

        for spin_box in self.spin_boxes:
            spin_box.blockSignals(False)

    def save_labels(self):
        labels = {}
        ann_info = {}
        save_dict = {}
        for i in range(len(self.current_objects)):
            labels[i] = self.current_objects[i]

        ann_info["sync_offsets"] = self.sync_offsets
        save_dict["ann_info"] = ann_info
        save_dict["annotations"] = labels
        
        save_file = self.hand_labels + self.image_id + ".json"
        with open(save_file, 'w') as file:
            json.dump(save_dict, file, sort_keys=True, indent=4)


    def delete_labels(self):
        file_name = self.hand_labels + self.image_id + ".json"
        if os.path.exists(file_name):
            os.remove(file_name)

    def estimate_labels(self):
        annotations = get_annotations(self.image_idx, self.auto_labels)
        self.current_objects = []
        for annotation in annotations:
            ground_pt = annotation['rough_ground_pt']
            try:
                location = ground_pt[0]
                self.create_new_object(location)
            except:
                location = ground_pt
                self.create_new_object(location)

    def init_labels(self):
        file_name = self.hand_labels + self.image_id + ".json"
        prev_id = self.image_list[self.image_idx-1]
        prev_file_name = self.hand_labels + prev_id + ".json"
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                labels = json.load(file)
        elif os.path.exists(prev_file_name):
            with open(prev_file_name, "r") as file:
                labels = json.load(file)
        else:
            print("[INFO] No prior labels")
            labels = {}

        self.current_objects = []
        for key, val in labels["annotations"].items():
            self.current_objects.append(val)
        
        self.sync_offsets = labels["ann_info"]["sync_offsets"]
        self.update_spin_params()
        self.update()

    def load_labels(self):
        file_name = self.hand_labels + self.image_id + ".json"
        if os.path.exists(file_name):
            with open(file_name) as file:
                labels = json.load(file)
        else:
            labels = None
        
        self.current_objects = []
        if labels is not None:
            for key, val in labels["annotations"].items():
                self.current_objects.append(val)

            self.sync_offsets = labels["ann_info"]["sync_offsets"]
        self.update_spin_params()
        self.update()

    def draw_labels(self):
        if self.calib is None:
            self.calib = []
            for cam in self.cams:
                calib_path = "data/wibam/calib/calibration_{}.npz".format(cam)
                self.calib.append(np.load(calib_path))
        self.drawnon_images = copy.deepcopy(self.current_images)
        self.drawnon_images, boxGndPoints, boxImgPoints = draw_3D_labels(
            self.drawnon_images,
            self.current_objects,
            self.calib
        )
        idx = -1
        for i in range(len(self.current_objects)):
            if self.current_objects[i]['current']:
                idx = i
        if idx < 0:
            return
        if self.imageSpinBox.value() > 3:
            return
        img_points = boxImgPoints[self.imageSpinBox.value(),idx]
        gnd_points = boxGndPoints[idx]
        self.FLpoint.setText("{}".format(img_points[0]))
        self.FRpoint.setText("{}".format(img_points[1]))
        self.RLpoint.setText("{}".format(img_points[3]))
        self.RRpoint.setText("{}".format(img_points[2]))
        self.FRpointGround.setText("{}".format(gnd_points[0]))
        self.FLpointGround.setText("{}".format(gnd_points[1]))
        self.RLpointGround.setText("{}".format(gnd_points[3]))
        self.RRpointGround.setText("{}".format(gnd_points[2]))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
