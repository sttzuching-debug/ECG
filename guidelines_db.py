# guidelines_db.py

CLINICAL_GUIDELINES = {
    "IVCD": {
        "title": "心室內傳導障礙 (AHA/ACCF/HRS 2009)",
        "criteria": "成人 QRS ≥ 120ms 為完全阻滯；110-119ms 為不完全阻滯 [cite: 59, 78, 90]。",
        "rbbb": "V1/V2 出現 rsR' 波，且 I/V6 S波寬於 R波 [cite: 79, 85]。",
        "lbbb": "I, aVL, V5, V6 出現寬且有切跡的 R波，且 q波消失 [cite: 97, 98]。"
    },
    "ACS": {
        "title": "急性冠心症處置 (ACS Guidelines)",
        "stemi": {
            "strategy": "啟動心導管室，目標 FMC 到 PCI < 120 分鐘。",
            "meds": [
                "Aspirin: 160-325 mg 咬碎吞服 (初期劑量)",
                "NTG: 0.4 mg 舌下含服 (需確認 SBP > 90 且無右心梗塞)",
                "P2Y12 抑制劑: Clopidogrel 300-600 mg 或 Ticagrelor 180 mg"
            ]
        }
    },
    "AFib": {
        "title": "心房顫動處置 (2023 ACC/AHA/ACCP/HRS)",
        "unstable": "血流動力學不穩：準備同步電擊整流 (Synchronized Cardioversion)。",
        "rate_control": {
            "meds": [
                "Diltiazem: 0.25 mg/kg IV (2 mins)，必要時 15 分鐘後追加 0.35 mg/kg。",
                "Amiodarone (心衰竭首選): 150 mg IV 滴注 10 分鐘。"
            ]
        },
        "anticoagulation": "CHA2DS2-VASc ≥ 2 (男) / ≥ 3 (女) 強烈建議使用 DOAC。"
    },
    "VA": {
        "title": "心室心律不整 (2017 AHA/ACC/HRS)",
        "tdp": {
            "strategy": "多型性 VT 且 QTc 延長，高度懷疑 Torsades de Pointes。",
            "meds": ["Magnesium Sulfate: 1-2 g 稀釋於 10 mL D5W，15 分鐘內 IV 推注。"]
        },
        "monomorphic_vt": {
            "meds": ["Amiodarone: 150 mg 溶於 100 mL D5W，滴注 10 分鐘。"]
        }
    }
}
