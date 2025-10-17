import pandas as pd
import os
from datetime import datetime

def daily_report():
    # Attendance CSV file
    attendance_file = "attendance.csv"
    
    if not os.path.exists(attendance_file):
        print("⚠️ No attendance records found.")
        return
    
    # Read attendance CSV (force pandas NOT to use pyarrow)
    df = pd.read_csv(attendance_file, engine="python")
    
    # Filter today's records
    today = datetime.now().strftime("%Y-%m-%d")
    daily = df[df["Date"] == today]

    print("\nToday's Attendance:")
    print(daily)

    # Save daily report
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)

    out_xlsx = os.path.join(reports_dir, f"Attendance_{today}.xlsx")
    out_csv = os.path.join(reports_dir, f"Attendance_{today}.csv")

    try:
        # Save to Excel (requires openpyxl)
        daily.to_excel(out_xlsx, index=False, engine="openpyxl")
        print(f"\n Report saved as Excel: {out_xlsx}")
    except ImportError:
        # If openpyxl not installed, fallback to CSV
        daily.to_csv(out_csv, index=False)
        print(f"\n⚠️ openpyxl not found. Report saved as CSV instead: {out_csv}")

if __name__ == "__main__":
    daily_report()
