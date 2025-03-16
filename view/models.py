from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import QAbstractListModel, Qt, QStringListModel
from utill import bean


class SchoolModel(QAbstractListModel):
    def __init__(self, schools: list[bean.School]):
        super().__init__()
        self.schools = schools or []
        self.filter_schools = schools or []

    def rowCount(self, parent):
        return len(self.filter_schools)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.filter_schools[index.row()].name
        return None

    def loadSchools(self, schools: list[bean.School]):
        self.schools = schools
        self.filter_schools = schools
        self.layoutChanged.emit()

    def getSchool(self, index):
        return self.filter_schools[index]

    def filt(self, school_name: str):
        self.filter_schools = [
            school for school in self.schools if school_name in school.name
        ]
        self.layoutChanged.emit()
