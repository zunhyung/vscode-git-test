# -*- coding: utf-8 -*-
"""Untitled61.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HziqlsHeR1RggMLSuJITN2EVXyjkANf5
"""

import random

class 시간표배정기:
    def __init__(self):
        self.timetable = [[None] * 5 for _ in range(6)]

    def 자동_수업_배정(self, 교수):
        for _ in range(100):
            day, time = random.randint(0, 5), random.randint(0, 4)
            if self.timetable[day][time] is None and sum(row.count(professor) for row in self.timetable) < 3:
                self.시간표[day][time] = professor
                return True
        return False

# 사용 예시:
scheduler  = TimetableScheduler()
professorname = "professorA"

success  = scheduler.auto_assign_course(professor_name)
if success:
    print(f"{교수명}님의 수업이 배정되었습니다.")
else:
    print("수업 배정에 실패했습니다. 교수님의 일정 또는 슬롯의 가용성을 확인해주세요.")