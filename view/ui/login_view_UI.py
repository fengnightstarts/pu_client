# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_view.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QSpacerItem,
    QStatusBar,
    QToolBar,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 379)
        self.flush_school_lists_action = QAction(MainWindow)
        self.flush_school_lists_action.setObjectName("flush_school_lists_action")
        self.flush_school_lists_action.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.formLayout.setVerticalSpacing(13)
        self.username_Label = QLabel(self.centralwidget)
        self.username_Label.setObjectName("username_Label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.username_Label)

        self.username_LineEdit = QLineEdit(self.centralwidget)
        self.username_LineEdit.setObjectName("username_LineEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.username_LineEdit)

        self.password_Label = QLabel(self.centralwidget)
        self.password_Label.setObjectName("password_Label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.password_Label)

        self.password_LineEdit = QLineEdit(self.centralwidget)
        self.password_LineEdit.setObjectName("password_LineEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.password_LineEdit)

        self.school_Label = QLabel(self.centralwidget)
        self.school_Label.setObjectName("school_Label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.school_Label)

        self.school_ComboBox = QComboBox(self.centralwidget)
        self.school_ComboBox.setObjectName("school_ComboBox")
        self.school_ComboBox.setEditable(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.school_ComboBox)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.formLayout.setItem(0, QFormLayout.FieldRole, self.verticalSpacer_2)

        self.verticalLayout_2.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_on_hand_RadioButton = QRadioButton(self.centralwidget)
        self.login_on_hand_RadioButton.setObjectName("login_on_hand_RadioButton")
        self.login_on_hand_RadioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.login_on_hand_RadioButton)

        self.auto_loginRadioButton = QRadioButton(self.centralwidget)
        self.auto_loginRadioButton.setObjectName("auto_loginRadioButton")

        self.horizontalLayout.addWidget(self.auto_loginRadioButton)

        self.use_this_token_RadioButton = QRadioButton(self.centralwidget)
        self.use_this_token_RadioButton.setObjectName("use_this_token_RadioButton")

        self.horizontalLayout.addWidget(self.use_this_token_RadioButton)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.login_PushButton = QPushButton(self.centralwidget)
        self.login_PushButton.setObjectName("login_PushButton")

        self.verticalLayout_2.addWidget(self.login_PushButton)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.flush_school_lists_action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.flush_school_lists_action.setText(
            QCoreApplication.translate(
                "MainWindow", "\u5237\u65b0\u5b66\u6821\u5217\u8868", None
            )
        )
        self.username_Label.setText(
            QCoreApplication.translate("MainWindow", "\u7528\u6237\u540d", None)
        )
        self.password_Label.setText(
            QCoreApplication.translate("MainWindow", "\u5bc6\u7801", None)
        )
        self.school_Label.setText(
            QCoreApplication.translate("MainWindow", "\u5b66\u6821", None)
        )
        self.label.setText(
            QCoreApplication.translate("MainWindow", "\u5b66\u6821\u540d\u79f0", None)
        )
        self.login_on_hand_RadioButton.setText(
            QCoreApplication.translate("MainWindow", "\u624b\u52a8\u767b\u5f55", None)
        )
        self.auto_loginRadioButton.setText(
            QCoreApplication.translate("MainWindow", "\u81ea\u52a8\u767b\u5f55", None)
        )
        # if QT_CONFIG(tooltip)
        self.use_this_token_RadioButton.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>\u4e0b\u6b21\u7ee7\u7eed\u4f7f\u7528\u672c\u6b21\u83b7\u53d6\u5230\u7684token\u800c\u4e0d\u518d\u8bf7\u6c42\u767b\u5f55\uff0c\u82e5\u83b7\u53d6\u6d3b\u52a8\u5217\u8868\u5931\u8d25\u5c06\u8fd4\u56de\u8be5\u754c\u9762\u3002</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.use_this_token_RadioButton.setText(
            QCoreApplication.translate("MainWindow", "\u8bb0\u4f4ftoken", None)
        )
        self.login_PushButton.setText(
            QCoreApplication.translate("MainWindow", "\u767b\u5f55", None)
        )
        self.toolBar.setWindowTitle(
            QCoreApplication.translate("MainWindow", "toolBar", None)
        )

    # retranslateUi
