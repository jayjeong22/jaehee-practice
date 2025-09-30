import streamlit as st

st.title("오늘의 목표 관리 앱")
st.write("오늘 이루고 싶은 목표를 작성하고, 달성하면 체크해보세요!")

# 1. 오늘의 목표 3가지 작성
goals = []
for i in range(1, 4):
	goal = st.text_input(f"오늘의 목표 {i}", key=f"goal_{i}")
	goals.append(goal)

# 2. 목표별 완료 체크박스
completed = []
for i, goal in enumerate(goals):
	if goal:
		checked = st.checkbox(f"목표 {i+1}: {goal}", key=f"check_{i}")
		completed.append(checked)

# 3. 목표 모두 완료 시 응원 멘트
if goals and all(goal for goal in goals) and all(completed) and len(completed) == 3:
	st.success("🎉 모든 목표를 달성했어요! 오늘도 수고 많았어요! 👏")
