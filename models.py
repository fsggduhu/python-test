"""
定义基类及继承子类，包含封装、继承与多态特性。
"""

class Person:
    """人员基类，包含基本属性"""
    def __init__(self, name: str, age: int, email: str, phone: str):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

    def display_info(self) -> str:
        """多态基准方法"""
        return f"姓名: {self.name}, 年龄: {self.age}, 手机: {self.phone}, 邮箱: {self.email}"


class Teacher(Person):
    """教师类，继承自 Person"""
    def __init__(self, emp_id: str, name: str, age: int, email: str, phone: str):
        super().__init__(name, age, email, phone)
        self.__emp_id = emp_id

    @property
    def emp_id(self) -> str:
        return self.__emp_id

    def display_info(self) -> str:
        """多态：重写，教师特有的信息展示"""
        base_info = super().display_info()
        return f"[教师端] 教工号: {self.emp_id} | {base_info}"


class Student(Person):
    """学生类，继承自 Person"""
    def __init__(
        self, student_id: str, name: str, age: int,
        email: str, phone: str, grades: dict = None
    ):
        super().__init__(name, age, email, phone)
        self.__student_id = student_id
        self.grades = grades if grades is not None else {}

    @property
    def student_id(self) -> str:
        """提供学号的只读访问接口"""
        return self.__student_id

    def add_grade(self, subject: str, score: float):
        """添加或修改单科成绩"""
        self.grades[subject] = float(score)

    def delete_grade(self, subject: str) -> bool:
        """删除单科成绩"""
        if subject in self.grades:
            del self.grades[subject]
            return True
        return False

    def get_average_grade(self) -> float:
        """计算均分"""
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

    def get_total_grade(self) -> float:
        """计算总分"""
        return sum(self.grades.values())

    def display_info(self) -> str:
        """多态：重写方法，增加学生特有字段"""
        base_info = super().display_info()
        avg = self.get_average_grade()
        return f"[学生端] 学号: {self.student_id} | {base_info} | 均分: {avg:.2f}"

    def to_dict(self) -> dict:
        """序列化为字典，供 JSON 保存使用"""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "phone": self.phone,
            "email": self.email,
            "grades": self.grades
        }