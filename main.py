"""
主程序入口 (main.py)
包含权限分离逻辑（教师/学生双视图）、复杂业务交互及菜单路由。
"""

from prettytable import PrettyTable
from config import TEACHER_PWD, PASSING_SCORE
from models import Student, Teacher
from storage import load_data, save_data, export_to_csv, write_log, fetch_daily_quote, read_logs
from utils import (
    validate_email, validate_age, validate_phone,
    quick_sort_students, binary_search_student, calc_fibonacci_points, print_separator
)

class StudentManagerSystem:
    def __init__(self):
        self.students = load_data()
        self.all_subjects = set()
        self._sync_subjects()
        write_log("系统启动", "System")

    def _sync_subjects(self):
        """动态同步系统中存在的所有学科种类"""
        self.all_subjects.clear()
        for student in self.students.values():
            for subject in student.grades.keys():
                self.all_subjects.add(subject)

    def _render_table(self, student_list) -> str:
        """第三方库应用：生成美化数据表格"""
        if not student_list:
            return "- 暂无数据 -"

        table = PrettyTable()
        table.field_names =["学号", "姓名", "年龄", "手机号", "平均分", "成绩明细"]
        for s in student_list:
            avg_str = f"{s.get_average_grade():.2f}"
            grades_str = ", ".join([f"{k}:{v}" for k, v in s.grades.items()])
            table.add_row([s.student_id, s.name, s.age, s.phone, avg_str, grades_str if grades_str else "无记录"])
        return str(table)

    # ================= 权限1：教师专属核心功能 =================
    def add_new_student(self):
        print_separator("添加学生信息")
        sid = input("- 请输入新学号: ").strip()
        if sid in self.students:
            print("- 【失败】该学号已存在。")
            return

        name = input("- 请输入姓名: ").strip()

        while True:
            age_input = input("- 请输入年龄: ").strip()
            is_valid, result = validate_age(age_input)
            if is_valid:
                age = result
                break
            print(f"【错误】{result}")

        while True:
            phone = input("请输入手机号: ").strip()
            if validate_phone(phone): break
            print("【错误】格式不正确，请输入11位大陆手机号。")

        while True:
            email = input("请输入邮箱: ").strip()
            if validate_email(email): break
            print("【错误】邮箱格式不合法。")

        self.students[sid] = Student(sid, name, age, email, phone)
        save_data(self.students)
        write_log(f"添加了学生: {sid} {name}", "Teacher")
        print(f"【成功】已录入学生: {name}")

    def edit_student_info(self):
        print_separator("修改学生信息")
        sid = input("请输入要修改的学号: ").strip()
        if sid not in self.students:
            print("【失败】查无此人。")
            return

        student = self.students[sid]
        print(f"当前信息: {student.display_info()}")

        new_phone = input("请输入新手机号 (直接回车表示不修改): ").strip()
        if new_phone:
            if validate_phone(new_phone):
                student.phone = new_phone
            else:
                print("【错误】手机号格式有误，修改跳过。")

        new_email = input("请输入新邮箱 (直接回车表示不修改): ").strip()
        if new_email:
            if validate_email(new_email):
                student.email = new_email
            else:
                print("【错误】邮箱格式有误，修改跳过。")

        save_data(self.students)
        write_log(f"编辑了学生信息: {sid}", "Teacher")
        print("【成功】信息更新完毕。")

    def delete_student(self):
        print_separator("删除学生记录")
        sid = input("请输入要删除的学号: ").strip()
        if sid in self.students:
            confirm = input(f"确定要删除 {self.students[sid].name} 吗？(y/n): ").strip().lower()
            if confirm == 'y':
                del self.students[sid]
                save_data(self.students)
                self._sync_subjects()
                write_log(f"删除了学生: {sid}", "Teacher")
                print("【成功】学生数据已删除。")
            else:
                print("操作已取消。")
        else:
            print("【失败】未找到该学号。")

    def manage_grades(self):
        print_separator("录入/修改学生成绩")
        sid = input("请输入目标学号: ").strip()
        if sid not in self.students:
            print("【失败】未找到该学号信息。")
            return

        student = self.students[sid]
        subject = input("请输入科目名称: ").strip()
        try:
            score = float(input("请输入分数 (0-100): ").strip())
            if not (0 <= score <= 100):
                raise ValueError("分数必须在 0 - 100 之间。")
            student.add_grade(subject, score)
            self._sync_subjects()
            save_data(self.students)
            write_log(f"修改了成绩 {sid} - {subject}: {score}", "Teacher")
            print("【成功】成绩处理完成！")
        except ValueError as e:
            print(f"【错误】无效分数: {e}")

    def search_student_binary(self):
        print_separator("查找学生")
        sid = input("请输入要查询的学号: ").strip()
        sorted_by_id = quick_sort_students(list(self.students.values()), key='id')
        found_student = binary_search_student(sorted_by_id, sid)

        if found_student:
            print("\n[精确查询结果]")
            print(found_student.display_info())
            print(self._render_table([found_student]))
        else:
            print("【失败】没有找到这个学号。")

    def analyze_subjects(self):
        print_separator("全校科目数据分析")
        if not self.all_subjects:
            print("当前暂无任何成绩记录。")
            return

        table = PrettyTable()
        table.field_names =["科目", "考试人数", "最高分", "最低分", "平均分", "及格率"]

        for sub in self.all_subjects:
            scores = [s.grades[sub] for s in self.students.values() if sub in s.grades]
            if scores:
                count = len(scores)
                max_s = max(scores)
                min_s = min(scores)
                avg_s = sum(scores) / count
                pass_count = len([x for x in scores if x >= PASSING_SCORE])
                pass_rate = f"{(pass_count / count) * 100:.1f}%"
                table.add_row([sub, count, max_s, min_s, f"{avg_s:.2f}", pass_rate])

        print(table)
        write_log("执行了全校成绩统计", "Teacher")

    # ================= 权限2：学生专属功能 =================
    def calculate_fibonacci(self, student: Student):
        print_separator("我的专属学习积分 (递归算法)")
        print("- 将根据您及格的科目数量，通过斐波那契数列计算奖励积分！")
        passed_subjects = len([s for s in student.grades.values() if s >= PASSING_SCORE])
        points = calc_fibonacci_points(passed_subjects + 3)
        print(f"- 您及格了 {passed_subjects} 个科目。")
        print(f"- 🎉 您的斐波那契积分为: {points} 分！继续加油！")

    def display_daily_quote(self):
        print_separator("🌟 每日一句")
        quote = fetch_daily_quote()
        print(f"👉 『 {quote} 』")

    # ================= 系统菜单控制 =================
    def teacher_menu(self, teacher: Teacher):
        """教师端无限循环主菜单"""
        while True:
            print_separator(f"教师端主菜单 - 欢迎", "=")
            # 在这里实际调用了 teacher 变量，证明“多态”和“封装”的存在意义！
            print(f"👋 您好，{teacher.name}老师！您的身份档案：")
            print(f"   {teacher.display_info()}")
            print("-" * 60)
            print(" -------- 1. ➕ 添加学生档案 -------- ")
            print(" -------- 2. ✏️ 修改学生档案 -------- ")
            print(" -------- 3. ❌ 删除学生档案 -------- ")
            print(" -------- 4. 📝 录入/修改成绩 ------- ")
            print(" -------- 5. 🔍 二分查找搜索 -------- ")
            print(" -------- 6. 📊 查看成绩排名 -------- ")
            print(" -------- 7. 📈 全校科目分析 -------- ")
            print(" -------- 8. 🗃️ 导出到 CSV  -------- ")
            print(" -------- 9. 📜 查看操作日志 -------- ")
            print(" -------- 0. 🚪  注销退出    -------- ")
            print("*" * 60)

            choice = input("请输入执行的操作 (0-9): ").strip()
            if choice == '1':
                self.add_new_student()
            elif choice == '2':
                self.edit_student_info()
            elif choice == '3':
                self.delete_student()
            elif choice == '4':
                self.manage_grades()
            elif choice == '5':
                self.search_student_binary()
            elif choice == '6':
                print_separator("全校排行榜")
                sorted_list = quick_sort_students(list(self.students.values()), key='average')
                print(self._render_table(sorted_list))
            elif choice == '7':
                self.analyze_subjects()
            elif choice == '8':
                if export_to_csv(self.students):
                    print("- 【成功】数据已保存至 CSV 中。")
            elif choice == '9':
                print_separator("最近系统操作日志")
                print(read_logs())
            elif choice == '0':
                write_log("教师注销退出", "Teacher")
                break
            else:
                print("【错误】操作无效，请重新输入。")

    def student_menu(self, student: Student):
        """学生端有限权限菜单"""
        self.display_daily_quote()
        while True:
            print_separator(f"学生端主菜单 - 欢迎{student.name}同学", "=")
            print(" -------- 1. 👤 查看我的档案与成绩 --------")
            print(" -------- 2. 🏆 查看全校成绩排行榜 --------")
            print(" -------- 3. 🎮 领取学习奖励积分   --------")
            print(" --------    0. 🚪 注销退出      --------")
            print("=" * 60)

            choice = input("请输入指令 (0-3): ").strip()
            if choice == '1':
                print_separator("我的个人档案")
                print(student.display_info())
                print(self._render_table([student]))
            elif choice == '2':
                print_separator("全校排行榜")
                sorted_list = quick_sort_students(list(self.students.values()), key='average')
                print(self._render_table(sorted_list))
            elif choice == '3':
                self.calculate_fibonacci(student)
            elif choice == '0':
                write_log(f"学生 {student.student_id} 注销", "Student")
                break
            else:
                print("- 【错误】指令无效。")

    def run(self):
        while True:
            print_separator("学生信息管理系统 - 身份认证", "★")
            print("  1. 👨‍🏫 教师通道")
            print("  2. 👨‍🎓 学生通道")
            print("  0. 🔴 关闭系统")
            print("★" * 60)

            role = input("请选择登录通道 (0-2): ").strip()

            if role == '1':
                pwd = input("- 请输入管理密码: ").strip()
                if pwd == TEACHER_PWD:
                    write_log("教师管理员登录成功", "System")
                    admin = Teacher("0011", "林知远", 28, "admin@school.edu", "13786663822")
                    self.teacher_menu(admin)
                else:
                    write_log("教师端密码尝试错误", "System")
                    print("- 【失败】密码错误，拒绝访问。")

            elif role == '2':
                sid = input(" 请输入您的学号: ").strip()
                if sid in self.students:
                    write_log(f"学生登录成功: {sid}", "System")
                    self.student_menu(self.students[sid])
                else:
                    print("【失败】系统中没有查到该学号。")

            elif role == '0':
                print_separator("系统正在关闭，正在执行最后的数据保存...", "★")
                save_data(self.students)
                write_log("系统正常关闭", "System")
                print("★ 感谢使用，再见！")
                break
            else:
                print("【错误】无效选项。")

if __name__ == '__main__':
    app = StudentManagerSystem()
    app.run()