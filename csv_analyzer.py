import pandas as pd
import json

def load_data(filename):
   return pd.read_csv(filename)

def analyze_data(df):
    total = len(df)

    by_country = df.groupby('country')["name"].count()

    completed = len(df[df["bet_status"] == "completed"])
    completion_rate = round(completed / total * 100, 2)

    return total, by_country, completion_rate
 

def save_report(total, by_country,completion_rate):
    report = {
        "总人数": total,
        "按国家分组": by_country.to_dict(), 
        "对赌完成率": f"{completion_rate}%"
    }
    with open("report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=4)

def main():
    df =  pd.read_csv("students.csv")     
    total, by_country, completion_rate = analyze_data(df)

    print(f"总人数: {total}")
    print(f"\n各国家人数:\n{by_country}")
    print(f"\n对赌完成率: {completion_rate}%")

    save_report(total, by_country, completion_rate)
    print("\n分析报告已保存到 report.json")

if __name__ == "__main__":
    main()
