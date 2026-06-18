# PU 活动助手

<p align="center">
  <img src="view/assets/auther_avatar.jpg" width="120" alt="PU 活动助手" />
</p>

<p align="center">
  <strong>轻松管理校园 PU 活动 — 智能筛选、自动报名、配置同步</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python" />
  <img src="https://img.shields.io/badge/GUI-PySide6-green.svg" alt="PySide6" />
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License" />
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg" alt="Platform" />
</p>

---

## 📖 简介

**PU 活动助手** 是一款基于 PySide6 的桌面客户端，专为高校学生设计，用于高效管理和参与 [PocketUni (PU)](https://pocketuni.net/) 校园活动。通过它，你可以：

- **一键登录** PU 平台，支持手动登录、自动登录、Token 复用三种方式
- **浏览全校活动**，查看活动详情、学分、容量、报名时间等关键信息
- **智能筛选**，按学院、年级、类别、容量、报名状态等多维度过滤活动
- **秒杀式报名**，定时精准抢报活动，多线程并发 + 指数退避重试
- **本地持久化**，自动保存登录凭据、筛选配置和报名列表
- **服务器同步**（可选），将报名任务同步至远程服务器，多设备协同

## 🖥️ 界面预览

| 登录界面 | 主界面 |
|:---:|:---:|
| 学校搜索 + 三种登录模式 | 活动卡片、多标签筛选、报名管理 |

主界面包含三个标签页：
- **全部活动** — 卡片式展示，包含活动封面、详情、一键报名/刷新
- **过滤结果** — 根据自定义条件实时过滤，只显示符合要求的活动
- **报名列表** — 管理已加入的报名任务，支持删除和状态追踪

## ✨ 核心功能

### 🔐 多模式登录
- **手动登录** — 输入学号密码，搜索并选择学校
- **自动登录** — 启动时自动使用保存的凭据登录
- **Token 登录** — 使用已有的 Token 直接进入主界面

### 🎯 活动筛选引擎

采用**装饰器模式**构建可组合的过滤器链，支持：

| 过滤器 | 说明 |
|:---|:---|
| 容量过滤 | 隐藏已满员的活动 |
| 报名状态 | 过滤未报名/已报名的活动 |
| 截止时间 | 隐藏已过报名截止时间的活动 |
| 类别过滤 | 按活动类别（文体、讲座等）筛选 |
| 学院过滤 | 只显示允许本学院参加的活动 |
| 年级过滤 | 只显示允许本年级参加的活动 |
| 报名方式 | 过滤需审核/无需审核的活动 |

### 🚀 智能报名系统

```
报名流程：
  ├── 定时调度器 — 在活动报名开放瞬间触发
  ├── 多线程并发 — 5 线程 × 2 轮（共 10 次尝试）
  ├── 指数退避 — 前 5 次 0.1s，中间 5 次 0.3s，后 5 次 0.5s
  └── 自动停止 — 任一线程成功即终止其余尝试
```

### 💾 配置管理

- 自动保存/加载 `user_data.json`
- 登录凭据（学号、密码、学校、Token）
- 筛选偏好（过滤方法、学院、年级、类别）
- 报名目标列表

### 🔗 服务器同步（可选）

支持与自建同步服务器通信：
- `POST /login` — 登录到同步服务器
- `POST /join` — 提交单个活动报名任务
- `POST /status` — 查询报名任务状态

## 📦 项目结构

```
pu_client/
├── main.py                  # 应用入口，启动 Qt 事件循环
├── requirements.txt         # 依赖列表
├── app/
│   ├── main.py              # 核心业务逻辑（消息处理、登录、报名）
│   └── scheduler_model.py   # 定时任务调度器（基于 schedule 库）
├── view/
│   ├── main_view.py         # 主窗口（活动展示、筛选、报名管理）
│   ├── login_view.py        # 登录窗口（学校搜索、凭据输入）
│   ├── log_view.py          # 日志窗口（实时运行日志）
│   ├── about_window.py      # 关于窗口（作者信息、GitHub 链接）
│   ├── theme.py             # 全局主题样式（Fusion 风格自定义 QSS）
│   ├── models.py            # Qt 数据模型（学校列表过滤）
│   ├── assets/              # 静态资源（头像等）
│   └── ui/                  # Qt Designer 生成的 UI 文件
├── utill/
│   ├── bean.py              # 数据类定义（User, Activity, Config 等）
│   ├── http_client.py       # HTTP 请求封装（同步 + 异步）
│   ├── filter.py            # 活动过滤器（装饰器模式）
│   ├── user_data_manager.py # 用户数据持久化
│   ├── urls.py              # API 端点
│   ├── headers.py           # HTTP 请求头
│   └── log_to_window.py     # 日志输出到 GUI 窗口
└── test/                    # 单元测试
```

## 🚀 快速开始

### 环境要求

- Python 3.8+
- Windows / Linux / macOS

### 安装

```bash
# 克隆仓库
git clone https://github.com/fengnightstarts/pu_client.git
cd pu_client

# 创建虚拟环境（推荐）
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# 安装依赖
pip install -r requirements.txt
```

### 运行

```bash
python main.py
```

### 打包为独立应用

```bash
pip install pyinstaller
pyinstaller main.spec
```

## 🛠️ 技术栈

| 技术 | 用途 |
|:---|:---|
| **PySide6** | Qt for Python GUI 框架 |
| **requests** | 同步 HTTP 请求 |
| **aiohttp** | 异步 HTTP 请求（活动详情并发获取） |
| **schedule** | 定时任务调度 |
| **threading / asyncio** | 多线程并发报名 |

### 架构设计

```
┌─────────────┐    消息队列(Queue)    ┌──────────────┐
│   GUI 线程   │ ◄──────────────────► │  业务逻辑线程  │
│  (PySide6)   │                      │  (app.main)   │
└─────────────┘                      └──────┬───────┘
                                            │
                              ┌─────────────┼─────────────┐
                              ▼             ▼             ▼
                        ┌──────────┐ ┌──────────┐ ┌──────────┐
                        │ 网络请求  │ │ 定时调度  │ │ 数据持久化│
                        │(http_cli)│ │(scheduler)│ │(user_data)│
                        └──────────┘ └──────────┘ └──────────┘
```

采用**生产者-消费者模型**，GUI 线程通过 `Queue` 与业务逻辑线程解耦通信：

1. GUI 触发操作（点击登录、报名等）
2. 封装为 `Message` 对象推入队列
3. 业务线程循环消费消息，执行网络请求
4. 结果通过 Signal/Slot 机制回传 UI 线程更新界面

## ⚠️ 免责声明

本项目仅供**学习与技术研究**使用，请勿用于任何违反 PocketUni 平台服务条款的行为。使用者需自行承担因使用本工具产生的一切后果。

## 👤 作者

**星夜不荟** — [GitHub @fengnightstarts](https://github.com/fengnightstarts)

如果你觉得这个工具对你有帮助，欢迎点一个 ⭐ Star！

## 📄 License

MIT License — 详见 [LICENSE](LICENSE) 文件。
