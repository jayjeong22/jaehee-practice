
import streamlit as st
import os


st.title("🌀 오늘의 목표 관리 앱 #madeby재희")
st.write("오늘 이루고 싶은 목표를 작성하고, 달성하면 체크해보세요." \
" 설정한 목표 3개를 모두 이루면 선물이 있습니다!")

# 1. 오늘의 목표 예시 칸 추가
with st.expander("뭘 적어야 할지 모르겠다면?"):
	st.markdown("""
	- 물 8잔 마시기
	- 30분 운동하기
	- 독서 20페이지
	- 감사한 일 3가지 적기
	- 일찍 자기
	- 산책하기
	- 업무/과제 마감
	- 건강식 먹기
	- 명상 10분
	""")

# 2. 오늘의 목표 3가지 작성
goals = []

# 더 부드러운 목표 입력 타이틀
goal_titles = [
	"오늘 꼭 해보고 싶은 일은?",
	"오늘 나를 위해 할 수 있는 일은?",
	"오늘 마무리하고 싶은 일은?"
]
for i in range(3):
	goal = st.text_input(goal_titles[i], key=f"goal_{i}")
	goals.append(goal)


# 3. 목표별 완료 체크박스 + 취소선 + 폭죽만
completed = []


for i, goal in enumerate(goals):
	if goal:
		checked = st.checkbox(goal, key=f"check_{i}")
		completed.append(checked)
		if checked:
			st.markdown(f"<s>{goal}</s>", unsafe_allow_html=True)
			st.balloons()

# 4. 목표 모두 완료 시 응원 멘트


# 4. 목표 모두 완료 시 응원 멘트
if goals and all(goal for goal in goals) and all(completed) and len(completed) == 3:
	st.success("🎉 모든 목표를 달성했어요! 사실 선물은 없습니다. 진정한 선물은 바로 당신입니다. 👏")


# --- 하단: 친구에게 공유하기 버튼 ---
st.markdown("---")
st.subheader("열정있는 매일을 이 어플과 함께하세요! 친구에게 공유하기")
share_url = "https://share.streamlit.io/jayjeong22/jaehee-practice/main/streamlit_app.py"
st.code(share_url, language=None)
st.info("위 링크를 복사해 친구에게 공유하세요!")

# --- 하단: 개발자에게 칭찬의 한 마디 남기기 ---
import os
st.markdown("---")
st.subheader("개발자에게 칭찬의 한 마디 남기기")
with st.form("praise_form"):
	praise_msg = st.text_area("개발자가 코딩을 계속 할 수 있도록 용기를 주세요 :)", max_chars=200)
	submitted = st.form_submit_button("메시지 남기기")
	if submitted and praise_msg.strip():
		# 메시지를 파일에 저장
		praise_file = "dev_praise.txt"
		with open(praise_file, "a", encoding="utf-8") as f:
			f.write(praise_msg.strip() + "\n")
		st.success("칭찬 메시지가 개발자에게 전달되었습니다! 감사합니다 😊")


