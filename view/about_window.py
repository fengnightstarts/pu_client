from pathlib import Path

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices, QPixmap
from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


PROJECT_URL = "https://github.com/fengnightstarts/pu_client/"
ASSETS_DIR = Path(__file__).resolve().parent / "assets"


def find_avatar_path():
    desktop = Path.home() / "Desktop"
    downloads = Path.home() / "Downloads"
    pictures = Path.home() / "Pictures"
    candidates = [
        ASSETS_DIR / "author_avatar.jpg",
        ASSETS_DIR / "author_avatar.png",
        ASSETS_DIR / "auther_avatar.jpg",
        ASSETS_DIR / "auther_avatar.png",
        desktop / "b_269102b8910780b11630344ca2296f7b.jpg",
    ]
    for folder in (desktop, downloads, pictures):
        if folder.exists():
            candidates.extend(folder.glob("b_*.jpg"))
            candidates.extend(folder.glob("b_*.png"))
            candidates.extend(folder.glob("*avatar*.jpg"))
            candidates.extend(folder.glob("*avatar*.png"))
            candidates.extend(folder.glob("*头像*.jpg"))
            candidates.extend(folder.glob("*头像*.png"))
    for path in candidates:
        if path.exists():
            return path
    return None


class AboutWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("支持作者")
        self.setModal(False)
        self.setMinimumSize(600, 420)
        self.resize(640, 460)
        self.__setup_ui()

    def __setup_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(40, 30, 40, 28)
        root.setSpacing(18)

        eyebrow = QLabel("ABOUT")
        eyebrow.setObjectName("AboutEyebrow")
        eyebrow.setAlignment(Qt.AlignCenter)
        root.addWidget(eyebrow)

        title = QLabel("PU 活动助手")
        title.setObjectName("AboutTitle")
        title.setAlignment(Qt.AlignCenter)
        root.addWidget(title)

        subtitle = QLabel("简单高效的 PU 活动筛选、报名与配置管理工具")
        subtitle.setObjectName("AboutSubtitle")
        subtitle.setAlignment(Qt.AlignCenter)
        root.addWidget(subtitle)

        content = QHBoxLayout()
        content.setSpacing(32)
        content.setContentsMargins(0, 18, 0, 8)

        text_box = QVBoxLayout()
        text_box.setSpacing(10)
        thanks = QLabel("感谢 星夜不荟")
        thanks.setObjectName("AboutThanks")
        body = QLabel(
            "如果这个工具帮你省下了抢活动、筛活动的时间，欢迎去 GitHub 给作者点一个 Star。"
        )
        body.setObjectName("AboutBody")
        body.setWordWrap(True)
        text_box.addWidget(thanks)
        text_box.addWidget(body)
        text_box.addStretch(1)

        avatar = QLabel()
        avatar.setObjectName("AuthorAvatar")
        avatar.setAlignment(Qt.AlignCenter)
        avatar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        avatar.setWordWrap(True)
        avatar_path = find_avatar_path()
        if avatar_path:
            avatar.setObjectName("AuthorAvatarImage")
            pixmap = QPixmap(str(avatar_path))
            scaled = pixmap.scaled(132, 132, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            avatar.setFixedSize(scaled.size())
            avatar.setPixmap(scaled)
        else:
            avatar.setFixedSize(132, 132)
            avatar.setText("未找到头像")

        content.addLayout(text_box, 1)
        content.addWidget(avatar, 0, Qt.AlignVCenter | Qt.AlignRight)
        root.addLayout(content)

        actions = QHBoxLayout()
        actions.setSpacing(10)
        actions.addStretch(1)
        star_button = QPushButton("Star on GitHub")
        star_button.setObjectName("PrimaryPillButton")
        star_button.clicked.connect(self.open_project)
        close_button = QPushButton("关闭")
        close_button.setObjectName("PillButton")
        close_button.clicked.connect(self.close)
        actions.addWidget(star_button)
        actions.addWidget(close_button)
        actions.addStretch(1)
        root.addLayout(actions)

        footer = QLabel("使用声明：本项目仅供学习与个人效率用途。")
        footer.setObjectName("AboutFooter")
        footer.setAlignment(Qt.AlignCenter)
        root.addWidget(footer)

    def open_project(self):
        QDesktopServices.openUrl(QUrl(PROJECT_URL))


def show_about_window(parent=None):
    window = AboutWindow(parent)
    window.show()
    window.raise_()
    window.activateWindow()
    return window
