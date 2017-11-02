# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IB_PyQt_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1272, 753)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setSizeIncrement(QtCore.QSize(10, 10))
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/IB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AnimatedDocks|QtWidgets.QMainWindow.GroupedDragging)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tabWidget.addTab(self.tab_8, "")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget_3.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_3.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_3.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1272, 26))
        self.menubar.setObjectName("menubar")
        self.menuLogin = QtWidgets.QMenu(self.menubar)
        self.menuLogin.setObjectName("menuLogin")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setAcceptDrops(True)
        self.dockWidget.setWindowIcon(icon)
        self.dockWidget.setFloating(False)
        self.dockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBox = QtWidgets.QToolBox(self.dockWidgetContents)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 246, 512))
        self.page.setObjectName("page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 246, 512))
        self.page_2.setObjectName("page_2")
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 246, 512))
        self.page_3.setObjectName("page_3")
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 246, 512))
        self.page_4.setObjectName("page_4")
        self.toolBox.addItem(self.page_4, "")
        self.verticalLayout.addWidget(self.toolBox)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.dockWidget_2 = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_2.sizePolicy().hasHeightForWidth())
        self.dockWidget_2.setSizePolicy(sizePolicy)
        self.dockWidget_2.setAcceptDrops(True)
        self.dockWidget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dockWidget_2.setFloating(False)
        self.dockWidget_2.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockWidget_2.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.dockWidgetContents_2)
        self.tabWidget_2.setAcceptDrops(True)
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget_2.setMovable(True)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.gridLayout_2.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_2)
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Images/ib-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionAbout.setIcon(icon1)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout_QT = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Images/Qt.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/Images/Qt.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionAbout_QT.setIcon(icon2)
        self.actionAbout_QT.setObjectName("actionAbout_QT")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Images/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionOpen.setIcon(icon3)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionSave.setIcon(icon4)
        self.actionSave.setObjectName("actionSave")
        self.actionLogin_to_account = QtWidgets.QAction(MainWindow)
        self.actionLogin_to_account.setObjectName("actionLogin_to_account")
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Images/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionNew.setIcon(icon5)
        self.actionNew.setObjectName("actionNew")
        self.actionTest_Connection = QtWidgets.QAction(MainWindow)
        self.actionTest_Connection.setObjectName("actionTest_Connection")
        self.actionZoom_In = QtWidgets.QAction(MainWindow)
        self.actionZoom_In.setObjectName("actionZoom_In")
        self.actionZoom_Out = QtWidgets.QAction(MainWindow)
        self.actionZoom_Out.setObjectName("actionZoom_Out")
        self.actionControl = QtWidgets.QAction(MainWindow)
        self.actionControl.setObjectName("actionControl")
        self.actionMessages = QtWidgets.QAction(MainWindow)
        self.actionMessages.setObjectName("actionMessages")
        self.actionText_Data = QtWidgets.QAction(MainWindow)
        self.actionText_Data.setObjectName("actionText_Data")
        self.actionGet_Data_From_Quandl = QtWidgets.QAction(MainWindow)
        self.actionGet_Data_From_Quandl.setObjectName("actionGet_Data_From_Quandl")
        self.actionGet_Data_From_Local_Database = QtWidgets.QAction(MainWindow)
        self.actionGet_Data_From_Local_Database.setObjectName("actionGet_Data_From_Local_Database")
        self.menuLogin.addAction(self.actionConnect)
        self.menuLogin.addAction(self.actionLogin_to_account)
        self.menuLogin.addAction(self.actionTest_Connection)
        self.menuLogin.addSeparator()
        self.menuLogin.addAction(self.actionGet_Data_From_Quandl)
        self.menuLogin.addAction(self.actionGet_Data_From_Local_Database)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_QT)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuView.addAction(self.actionZoom_In)
        self.menuView.addAction(self.actionZoom_Out)
        self.menuWindow.addAction(self.actionControl)
        self.menuWindow.addAction(self.actionMessages)
        self.menuWindow.addAction(self.actionText_Data)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuLogin.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionAbout)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(3)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IB_PyQt"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "Tab 2"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuLogin.setTitle(_translate("MainWindow", "Login"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Control"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Page 1"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Page 2"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Page"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("MainWindow", "Page"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Tab 1"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Tab 2"))
        self.actionConnect.setText(_translate("MainWindow", "Connect To IB"))
        self.actionAbout.setText(_translate("MainWindow", "About IB_PyQt"))
        self.actionAbout_QT.setText(_translate("MainWindow", "About QT"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionLogin_to_account.setText(_translate("MainWindow", "Login To Your Account"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionTest_Connection.setText(_translate("MainWindow", "Test Connection With IB"))
        self.actionZoom_In.setText(_translate("MainWindow", "Zoom In"))
        self.actionZoom_Out.setText(_translate("MainWindow", "Zoom Out"))
        self.actionControl.setText(_translate("MainWindow", "Control"))
        self.actionMessages.setText(_translate("MainWindow", "Messages"))
        self.actionText_Data.setText(_translate("MainWindow", "Text Data"))
        self.actionGet_Data_From_Quandl.setText(_translate("MainWindow", "Get Data From Quandl"))
        self.actionGet_Data_From_Local_Database.setText(_translate("MainWindow", "Get Data From Local Database"))

import resource_rc