import streamlit as st
import pandas as pd
from datetime import datetime
from guidelines_db import CLINICAL_GUIDELINES

st.set_page_config(page_title="ECG 臨床決策輔助系統", layout="wide")

st.title("🏥 心電圖判讀與處置輔助系統")
st.caption("專為專科護理師設計 | 整合 AHA/ACC 最新臨床指引")

# 側邊欄：輸入方式
with st.sidebar:
    st.header("輸入設定")
    input_mode = st.radio("選擇模式", ["手動輸入參數", "照片/PDF 辨識 (開發中)"])

# 主畫面：參數輸入
with st.container():
    st.subheader("📊 臨床參數勾選")
    with st.form("ecg_form"):
        col1, col2 = st.columns(2)
        with col1:
            qrs = st.selectbox("QRS 寬度", ["正常 (<110ms)", "不完全阻滯 (110-119ms)", "完全阻滯 (≥120ms)"])
            rhythm = st.selectbox("節律特徵", ["規則", "完全不規則 (AFib)", "寬 QRS 頻脈 (VT)"])
        with col2:
            st_change = st.selectbox("ST-T 變化", ["無", "ST上升 (STEMI)", "ST下降", "T波尖聳/倒置"])
            hemo = st.radio("血流動力學", ["穩定", "不穩定 (休克/胸痛)"])
        
        submitted = st.form_submit_button("執行判讀與驗證")

# 邏輯判斷與顯示結果
if submitted:
    st.divider()
    # 範例邏輯：若為 STEMI
    if st_change == "ST上升 (STEMI)":
        res = CLINICAL_GUIDELINES["ACS"]["stemi"]
        st.error(f"🚨 判斷結果：{CLINICAL_GUIDELINES['ACS']['title']}")
        st.write(f"**建議策略：** {res['strategy']}")
        
        st.info("⚠️ 藥物核對表 (Medication Check)")
        for m in res['meds']:
            st.checkbox(m, key=m)
            
    # 匯出功能
    st.download_button(
        "📥 匯出臨床紀錄 (.txt)",
        data=f"時間: {datetime.now()}\n結果: {st_change}\n狀態: {hemo}",
        file_name=f"ECG_{datetime.now().strftime('%m%d_%H%M')}.txt"
    )
