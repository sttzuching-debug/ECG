import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. 安全地讀取 API Key (從 Streamlit Secrets)
try:
    genai.configure(api_key=st.secrets["api_key"])
except KeyError:
    st.error("請先在 Streamlit Secrets 中設定 API Key！")
    st.stop()

# 2. 設定模型參數 (選擇適合視覺與文本的模型)
# 建議使用 gemini-1.5-pro，它的視覺解析與長脈絡能力最適合醫療影像
generation_config = {
  "temperature": 0.1, # 溫度調低，讓回答穩定、具備一致性，減少幻覺
  "top_p": 0.95,
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config
)

st.title("🏥 智能心電圖臨床決策輔助系統")

# ... (上傳照片的介面邏輯與先前相同) ...
uploaded_file = st.file_uploader("上傳 ECG 檔案 (JPG/PNG)", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="待判讀的心電圖影像", use_container_width=True)

    if st.button("🚀 啟動 AI 深度判讀"):
        with st.spinner("AI 正在解析影像與建立臨床決策路徑..."):
            
            # 3. 核心靈魂：防範幻覺的「系統提示詞 (System Prompt)」
            system_prompt = """
            你現在是一位在醫學中心工作的資深急診專科護理師導師。
            請分析這張心電圖影像，並且【嚴格遵循】以下三步思考框架來回答。若特徵不明顯或正常，請誠實回報正常，絕不可捏造危急病徵。

            [第一步：客觀數據提取]
            列出你觀察到的：心跳速率、節律是否規則、QRS 寬度 (預估 ms)、有無 ST 段變化、特定導程波形特徵。

            [第二步：臨床指引對應]
            根據上述客觀發現，這對應到哪一項指引？
            - 若為疑似 ACS：請引用 STEMI/NSTEMI 指引。
            - 若為心室內傳導障礙：請引用 AHA 2009 IVCD 指引。
            - 若為心律不整：請引用 2023 AFib 或 2017 VA 指引。
            - 若無異常：請明確指出「未觸發危急指引 (疑似正常 NSR)」。

            [第三步：下一步處置建議與護理重點]
            以條列式給出建議。若需給藥，請列出常見的標準劑量供護理人員「雙重核對」。
            """
            
            try:
                # 4. 呼叫 API，將圖片與提示詞一起送出
                response = model.generate_content([system_prompt, image])
                
                st.success("判讀完成！(結果僅供臨床參考，給藥前請覆核醫囑)")
                
                # 顯示 AI 回傳的結果
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"API 呼叫失敗，請檢查網路或金鑰狀態：{e}")
