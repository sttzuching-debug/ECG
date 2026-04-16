# guidelines_db.py

CLINICAL_GUIDELINES = {
    "ACS": {
        "source": "最新 ACS 臨床指引",
        "stemi_acomi": {
            "strategy": "目標在首次醫療接觸 (FMC) 後 120 分鐘內完成初次 PCI。若預估轉送時間過長且發作 < 12 小時，30 分鐘內評估血栓溶解劑。",
            "medication_check": [
                "💊 Aspirin: 160-325 mg 咬碎吞服 (若未曾服用)。",
                "💊 P2Y12 抑制劑: Ticagrelor 180 mg 或 Clopidogrel 300-600 mg (依醫囑)。",
                "💊 NTG: 0.4 mg 舌下含服 (每 5 分鐘一次，最多 3 次，需確認收縮壓 > 90 mmHg 且無右心梗塞)。"
            ]
        }
    },
    "AFib": {
        "source": "2023 ACC/AHA/ACCP/HRS Guideline",
        "stable_rate_control": {
            "strategy": "心室率過速 (>110 bpm) 且血流動力學穩定，優先進行速率控制。",
            "medication_check": [
                "💊 Diltiazem: 0.25 mg/kg 靜脈緩慢推注 (約 2 分鐘)，若無效 15 分鐘後可給予 0.35 mg/kg。",
                "💊 Amiodarone (若合併心衰竭): 150 mg 靜脈滴注超過 10 分鐘。"
            ]
        }
    },
    "VA": {
        "source": "2017 AHA/ACC/HRS Guideline",
        "monomorphic_stable": {
            "strategy": "具備結構性心臟病之寬 QRS 心搏過速，一律視為 VT 處理。準備同步電擊待命。",
            "medication_check": [
                "💊 Amiodarone: 150 mg 加入 100 mL D5W，靜脈滴注 10 分鐘。若發生低血壓需減慢滴速。",
                "💊 Procainamide: 20-50 mg/min 靜脈滴注，直到心律轉變或達最大劑量 17 mg/kg。"
            ]
        },
        "polymorphic_long_qt": {
            "strategy": "高度懷疑 Torsades de Pointes (TdP)。立即停用所有延長 QT 之藥物。",
            "medication_check": [
                "💊 硫酸鎂 (Magnesium Sulfate): 1-2 g 以 10 mL D5W 稀釋，於 15 分鐘內靜脈推注或滴注。"
            ]
        }
    }
}
