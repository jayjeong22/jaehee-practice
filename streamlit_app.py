
import streamlit as st

st.title("Streamlit 주요 요소 예시")  # 페이지 제목
st.caption("이 페이지는 Streamlit에서 사용할 수 있는 모든 주요 UI 요소의 예시를 보여줍니다.")  # 페이지 설명

# 텍스트 관련 요소
st.header("텍스트 요소")  # 헤더
st.subheader("서브헤더 예시")  # 서브헤더
st.text("일반 텍스트 예시")  # 일반 텍스트
st.markdown("**마크다운 텍스트** _예시_ [링크](https://streamlit.io)")  # 마크다운
st.code("print('Hello, Streamlit!')", language='python')  # 코드 블록
st.latex(r"E = mc^2")  # LaTeX 수식
st.caption("각주: 다양한 텍스트 및 마크다운 표현")

# 입력 위젯
st.header("입력 위젯")
name = st.text_input("이름을 입력하세요")  # 텍스트 입력
age = st.number_input("나이 입력", min_value=0, max_value=120)  # 숫자 입력
agree = st.checkbox("동의합니다")  # 체크박스
color = st.radio("좋아하는 색상은?", ["빨강", "파랑", "초록"])  # 라디오 버튼
option = st.selectbox("선택하세요", ["A", "B", "C"])  # 셀렉트박스
multi = st.multiselect("복수 선택", ["X", "Y", "Z"])  # 멀티셀렉트
date = st.date_input("날짜 선택")  # 날짜 입력
time = st.time_input("시간 선택")  # 시간 입력
file = st.file_uploader("파일 업로드")  # 파일 업로더
st.caption("각주: 다양한 입력 위젯")

# 버튼 및 상호작용
st.header("버튼 및 상호작용")
if st.button("버튼 클릭"):
    st.success("버튼이 클릭되었습니다!")
st.caption("각주: 버튼 클릭 시 동작 예시")

# 슬라이더
st.header("슬라이더")
slider_val = st.slider("값을 선택하세요", 0, 100, 50)
st.caption("각주: 슬라이더로 값 선택")

# 미디어 요소
st.header("미디어 요소")
st.image("https://static.streamlit.io/examples/dog.jpg", caption="강아지 이미지")  # 이미지
st.audio(
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    format="audio/mp3"
)  # 오디오
st.video(
    "https://www.w3schools.com/html/mov_bbb.mp4"
)  # 비디오
st.caption("각주: 이미지, 오디오, 비디오 등 미디어 요소")

# 데이터 표시
st.header("데이터 표시")
import pandas as pd
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
st.dataframe(df)  # 데이터프레임
st.table(df)  # 테이블
st.json({"key": "value", "number": 123})  # JSON
st.caption("각주: 데이터프레임, 테이블, JSON 표시")

# 차트
st.header("차트 예시")
import numpy as np
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)
st.line_chart(chart_data)  # 라인 차트
st.bar_chart(chart_data)  # 바 차트
st.area_chart(chart_data)  # 영역 차트
st.caption("각주: 기본 차트 예시")

# 상태 표시
st.header("상태 표시")
st.success("성공 메시지 예시")
st.info("정보 메시지 예시")
st.warning("경고 메시지 예시")
st.error("에러 메시지 예시")
st.caption("각주: 다양한 상태 메시지")

# 진행률 표시
st.header("진행률 표시")
import time
progress = st.progress(0)
for i in range(1, 101, 20):
    time.sleep(0.05)
    progress.progress(i)
st.caption("각주: 진행률 바 예시")

# 사이드바
st.sidebar.title("사이드바 예시")
st.sidebar.write("여기는 사이드바입니다.")
st.sidebar.button("사이드바 버튼")
st.caption("각주: 사이드바 활용")
