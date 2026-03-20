"""
系统配置文件 (config.py)
管理系统全局参数，包含路径、权限验证密钥、API地址等
"""
import os

# 基础目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 数据存储文件路径 (JSON格式)
DATA_FILE = os.path.join(BASE_DIR, "students_data.json")

# 导出的报表文件路径 (CSV格式)
CSV_EXPORT_FILE = os.path.join(BASE_DIR, "students_export.csv")

# 系统操作日志文件 (TXT格式)
LOG_FILE = os.path.join(BASE_DIR, "system_operation.log")

# 教师端超级管理密码 (避免硬编码)
TEACHER_PWD = "123456"

# 成绩及格线配置
PASSING_SCORE = 60.0