import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ページ設定
st.set_page_config(page_title="CSVデータ解析アプリ", layout="wide")
st.title("📊 CSVデータ解析アプリ")

# CSVアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])

if uploaded_file is not None:
    # CSV 読み込み
    df = pd.read_csv(uploaded_file)
    st.subheader("データプレビュー")
    st.dataframe(df.head())

    # 数値列を選択
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    if len(numeric_cols) == 0:
        st.warning("数値データが見つかりません。")
    else:
        col = st.selectbox("解析する数値列を選択してください", numeric_cols)

        # 基本統計量
        st.subheader("📈 基本統計量")
        st.write(df[col].describe())

        # ヒストグラム＋分布曲線
        st.subheader("📊 ヒストグラムと分布曲線")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.histplot(df[col], kde=True, bins=20, ax=ax)
        ax.set_title(f"{col} の分布", fontsize=14)
        st.pyplot(fig)