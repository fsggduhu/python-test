"""
工具与算法模块 (utils.py)
包含 UI 排版工具、正则校验、排序/查找算法及递归应用。
"""
import re
from typing import List,Tuple,Any
from models import Student

def print_separator(title: str = "", char: str = "-", width: int = 60):
    """UI 排版：打印分割线，美化输出独立成行"""
    print("\n" + char * width)
    if title:
        print(f" {title} ".center(width, char))
        print(char * width)

def validate_email(email: str) -> bool:
    """正则匹配：校验邮箱合法性"""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def validate_phone(phone: str) -> bool:
    """正则匹配：校验中国大陆手机号"""
    pattern = r'^1[3-9]\d{9}$'
    return bool(re.match(pattern, phone))

def validate_age(age_str: str) -> Tuple[bool, Any]:
    """数据校验：验证年龄"""
    try:
        age = int(age_str)
        if 0 < age < 100:
            return True, age
        return False, "年龄超出合理范围 (1-99)。"
    except ValueError:
        return False, "输入无效，必须是整数。"

def quick_sort_students(students: List[Student], key: str = 'average') -> List[Student]:
    """ 1：递归实现快速排序（按平均分或学号）"""
    if len(students) <= 1:
        return students

    base_point = students[len(students) // 2]

    if key == 'average':
        base_point_val = base_point.get_average_grade()
        left =[s for s in students if s.get_average_grade() > base_point_val]
        middle =[s for s in students if s.get_average_grade() == base_point_val]
        right =[s for s in students if s.get_average_grade() < base_point_val]
    else:
        # 按学号升序
        base_point_val = base_point.student_id
        left =[s for s in students if s.student_id < base_point_val]
        middle = [s for s in students if s.student_id == base_point_val]
        right = [s for s in students if s.student_id > base_point_val]

    return quick_sort_students(left, key) + middle + quick_sort_students(right, key)

def binary_search_student(sorted_students: List[Student], target_id: str) -> Student:
    """核心算法 2：二分查找（要求列表已按学号升序排列），时间复杂度 O(log N)"""
    left, right = 0, len(sorted_students) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_id = sorted_students[mid].student_id
        if mid_id == target_id:
            return sorted_students[mid]
        elif mid_id < target_id:
            left = mid + 1
        else:
            right = mid - 1
    return None

def calc_fibonacci_points(n: int) -> int:
    """递归演示：计算斐波那契数列，用于给学生计算隐藏的学习积分"""
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return calc_fibonacci_points(n - 1) + calc_fibonacci_points(n - 2)