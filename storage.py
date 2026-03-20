"""
数据存储模块 (storage.py)
负责 JSON 读写、CSV 导出、本地日志记录。
"""
import random
import json
import os
import csv
from datetime import datetime
from models import Student
from config import DATA_FILE, CSV_EXPORT_FILE, LOG_FILE

def write_log(action: str, operator: str = "System"):
    """写入系统操作日志"""
    try:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(f"[{now}] [{operator}] {action}\n")
    except Exception as e:
        print(f"【日志错误】写入日志失败: {e}")

def read_logs() -> str:
    """读取系统操作日志"""
    if not os.path.exists(LOG_FILE):
        return "- 暂无日志记录 -"
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception as e:
        return f"【日志错误】读取日志失败: {e}"

def load_data() -> dict:
    """读取并转换 JSON，异常处理捕获"""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            students = {}
            for sid,info in data.items():
                students[sid] = Student(
                    student_id=info.get('student_id', sid),
                    name=info.get('name', '未知'),
                    age=info.get('age', 0),
                    email=info.get('email', ''),
                    phone=info.get('phone', ''),
                    grades=info.get('grades', {})
                )
            return students
    except json.JSONDecodeError:
        print("【错误】JSON 文件格式损坏，将初始化为空。")
        return {}
    except PermissionError:
        print("【错误】无文件读取权限！")
        return {}

def save_data(students_dict: dict) -> bool:
    """序列化字典并写入 JSON 文件"""
    try:
        data = {sid: s.to_dict() for sid, s in students_dict.items()}
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except IOError as e:
        print(f"【错误】写入 JSON 文件发生异常: {e}")
        return False

def export_to_csv(students_dict: dict) -> bool:
    """导出学生成绩到 CSV 文件，展示了对另一种文件格式的处理能力"""
    try:
        with open(CSV_EXPORT_FILE, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            # 写入表头
            writer.writerow(['学号', '姓名', '年龄', '手机', '邮箱', '平均分', '总分', '所有成绩明细'])
            for s in students_dict.values():
                grades_str = "; ".join([f"{k}:{v}" for k, v in s.grades.items()])
                writer.writerow([
                    s.student_id, s.name, s.age, s.phone, s.email,
                    f"{s.get_average_grade():.2f}",
                    f"{s.get_total_grade():.2f}",
                    grades_str
                ])
        write_log(f"成功导出数据到 {CSV_EXPORT_FILE}", "Teacher")
        return True
    except Exception as e:
        print(f"【错误】导出 CSV 失败: {e}")
        return False


def fetch_daily_quote() -> str:
    """本地随机获取一句话励志名言 """
    quotes = [
        "保持热爱，奔赴山海。",
        "星光不问赶路人，时光不负有心人。",
        "路虽远，行则将至；事虽难，做则必成。",
        "长风破浪会有时，直挂云帆济沧海。",
        "既然选择了远方，便只顾风雨兼程。",
        "凡是过往，皆为序章。",
        "千川汇海阔，风好正扬帆。",
        "业精于勤，荒于嬉；行成于思，毁于随。",
        "宝剑锋从磨砺出，梅花香自苦寒来。",
        "不要让未来的你，讨厌现在不努力的自己。"
    ]

    # 使用 random.choice 从列表中随机抽取一句返回
    return random.choice(quotes)
