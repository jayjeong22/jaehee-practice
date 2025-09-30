import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("성적 데이터 시각화 앱")
st.write("CSV 파일을 업로드하고 다양한 그래프를 그릴 수 있습니다.")

# 1. CSV 파일 업로드
uploaded_file = st.file_uploader("성적 데이터 CSV 파일 업로드", type=["csv"])
df = None
if uploaded_file:
	df = pd.read_csv(uploaded_file)
	st.success("데이터 업로드 완료!")
	st.dataframe(df)

	# 2. 그래프 옵션 선택
	st.subheader("그래프 유형 선택")
	graph_type = st.radio(
		"원하는 그래프를 선택하세요",
		("히스토그램", "막대그래프", "산점도", "상자그림")
	)

	# 3. 변수 선택 및 맞춤형 그래프
	if graph_type == "히스토그램":
		num_cols = df.select_dtypes(include='number').columns.tolist()
		col = st.selectbox("히스토그램을 그릴 변수 선택", num_cols)
		if col:
			st.write(f"{col}의 히스토그램")
			fig, ax = plt.subplots()
			ax.hist(df[col].dropna(), bins=20, color='skyblue', edgecolor='black')
			ax.set_xlabel(col)
			ax.set_ylabel("빈도")
			st.pyplot(fig)
	elif graph_type == "막대그래프":
		cat_cols = df.select_dtypes(include='object').columns.tolist()
		num_cols = df.select_dtypes(include='number').columns.tolist()
		cat_col = st.selectbox("막대그래프의 범주형 변수 선택", cat_cols)
		num_col = st.selectbox("막대그래프의 수치형 변수 선택", num_cols)
		if cat_col and num_col:
			st.write(f"{cat_col}별 {num_col}의 평균 막대그래프")
			means = df.groupby(cat_col)[num_col].mean()
			fig, ax = plt.subplots()
			ax.bar(means.index.astype(str), means.values, color='orange')
			ax.set_xlabel(cat_col)
			ax.set_ylabel(f"{num_col} 평균")
			st.pyplot(fig)
	elif graph_type == "산점도":
		num_cols = df.select_dtypes(include='number').columns.tolist()
		x_col = st.selectbox("X축 변수 선택", num_cols)
		y_col = st.selectbox("Y축 변수 선택", num_cols, index=1 if len(num_cols)>1 else 0)
		if x_col and y_col:
			st.write(f"{x_col} vs {y_col} 산점도")
			fig, ax = plt.subplots()
			ax.scatter(df[x_col], df[y_col], alpha=0.7)
			ax.set_xlabel(x_col)
			ax.set_ylabel(y_col)
			st.pyplot(fig)
	elif graph_type == "상자그림":
		num_cols = df.select_dtypes(include='number').columns.tolist()
		col = st.selectbox("상자그림을 그릴 변수 선택", num_cols)
		if col:
			st.write(f"{col}의 상자그림")
			fig, ax = plt.subplots()
			ax.boxplot(df[col].dropna())
			ax.set_xlabel(col)
			st.pyplot(fig)

