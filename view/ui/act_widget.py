# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'act_widget.ui'
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
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QTextEdit,
    QWidget,
)


class Ui_act_Widget(object):
    def setupUi(self, act_Widget):
        if not act_Widget.objectName():
            act_Widget.setObjectName("act_Widget")
        act_Widget.resize(288, 203)
        act_Widget.setMinimumSize(QSize(160, 160))
        self.horizontalLayout_2 = QHBoxLayout(act_Widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.img_Label = QLabel(act_Widget)
        self.img_Label.setObjectName("img_Label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_Label.sizePolicy().hasHeightForWidth())
        self.img_Label.setSizePolicy(sizePolicy)
        self.img_Label.setMinimumSize(QSize(0, 0))
        self.img_Label.setMaximumSize(QSize(200, 200))

        self.horizontalLayout_2.addWidget(self.img_Label)

        self.teinfo_TextEdit = QTextEdit(act_Widget)
        self.teinfo_TextEdit.setObjectName("teinfo_TextEdit")
        self.teinfo_TextEdit.setEnabled(True)
        self.teinfo_TextEdit.setMinimumSize(QSize(80, 80))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.teinfo_TextEdit.setFont(font)
        self.teinfo_TextEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.teinfo_TextEdit)

        self.retranslateUi(act_Widget)

        QMetaObject.connectSlotsByName(act_Widget)

    # setupUi

    def retranslateUi(self, act_Widget):
        act_Widget.setWindowTitle(
            QCoreApplication.translate("act_Widget", "Form", None)
        )
        self.img_Label.setText("")

    # retranslateUi
