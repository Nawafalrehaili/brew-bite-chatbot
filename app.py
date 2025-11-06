import pandas as pd
import streamlit as st
import re

# --- تحميل البيانات ---
df = pd.read_csv("brew_bite_branches_arabic.csv")

# --- واجهة التطبيق ---
st.set_page_config(page_title="Brew & Bite شات بوت فروع", layout="centered")
st.title("🤖 شات بوت فروع Brew & Bite")

question = st.text_input("✏️ اكتب سؤالك:")

if question:
    # استخراج المدينة من السؤال
    branch_name = None
    for city in df['المدينة'].dropna().unique():
        if re.search(city, question, re.IGNORECASE):
            branch_name = city
            break

    if branch_name:
        # البحث عن الفرع بناءً على اسم المدينة أو الفرع
        row = df[
            df['المدينة'].str.contains(branch_name, na=False, case=False) |
            df['اسم الفرع'].str.contains(branch_name, na=False, case=False)
        ]

        if not row.empty:
            # توليد الرد بناءً على الكلمات المفتاحية
            response = "❓ لم أتمكن من تحديد نوع السؤال."

            if "مدير" in question:
                response = f"👤 مدير الفرع هو {row['اسم المدير'].values[0]}"
            elif "رقم" in question:
                response = f"📞 رقم المدير: {row['رقم المدير'].values[0]}"
            elif "دخل" in question or "مبيعات" in question:
                response = f"💰 الدخل الشهري للفرع هو {row['الدخل الشهري'].values[0]} ريال"
            elif "رضا" in question:
                response = f"📊 نسبة رضا العملاء: {row['رضا العملاء'].values[0]}"
            elif "وقت" in question or "دوام" in question:
                response = f"⏰ أوقات الدوام: {row['أوقات الدوام'].values[0]}"
            elif "منتج" in question:
                response = f"🧋 المنتج الأكثر مبيعًا: {row['المنتج الأكثر مبيعًا'].values[0]}"
            else:
                response = "📌 لم أتمكن من تحديد نوع السؤال بدقة."

            st.success(response)
        else:
            st.error("❌ لم يتم العثور على الفرع المطلوب.")
    else:
        st.warning("⚠️ يرجى تحديد المدينة في سؤالك.")
