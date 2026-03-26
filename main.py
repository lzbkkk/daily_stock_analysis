import json
import os
from datetime import datetime

# 确保文件夹存在
os.makedirs("reports", exist_ok=True)

# 生成 JSON 数据
json_data = {
    "name": "每日股票分析",
    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "stocks": ["600519", "000001"],
    "status": "success",
    "remark": "上传到 GitHub Release 成功"
}

# 写入文件
with open("reports/stock_analysis_latest.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)

print("✅ JSON 已生成：reports/stock_analysis_latest.json")
