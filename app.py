import pandas as pd
import streamlit as st

# تحميل البيانات
df = pd.read_csv("brew_bite_branches_arabic.csv")

# إعدادات الصفحة
st.set_page_config(page_title="شات بوت الفروع", page_icon="🤖", layout="centered")
st.title("🤖 شات بوت فروع Brew & Bite")
st.markdown("**اكتب سؤالك:**")

# إدخال المستخدم
question = st.text_input("", placeholder="كم دخل فرع جدة؟")

if question:
    # استخراج اسم المدينة
    city = ""
    for c in ["جدة", "الرياض", "مكة", "المدينة", "الدمام"]:
        if c in question:
            city = c
            break
    if not city:
        for c in ["jeddah", "riyadh", "makkah", "madinah", "dammam"]:
            if c.lower() in question.lower():
                city = c.lower()
                break

    translations = {
        "jeddah": "جدة",
        "riyadh": "الرياض",
        "makkah": "مكة",
        "madinah": "المدينة",
        "dammam": "الدمام"
    }
    if city in translations:
        city = translations[city]

    if not city:
        st.warning("⚠️ يرجى تحديد المدينة في سؤالك.")
    else:
        row = df[df["المدينة"] == city]
        if row.empty:
            st.error("❌ لم يتم العثور على الفرع المطلوب.")
        else:
            row = row.iloc[0]
            response = "❓ لم أتمكن من تحديد نوع السؤال."

            if "مدير" in question:
                response = f"👤 مدير الفرع هو: {row['اسم المدير']}"
            elif "رقم" in question:
                response = f"📞 رقم المدير: {row['رقم المدير']}"
            elif "دخل" in question or "مبيعات" in question:
                response = f"💰 الدخل الشهري للفرع هو: {row['الدخل الشهري']} ريال"
            elif "رضا" in question:
                response = f"📊 نسبة رضا العملاء: {row['رضا العملاء']}"
            elif "دوام" in question or "وقت" in question:
                response = f"⏰ أوقات الدوام: {row['أوقات الدوام']}"
            elif "منتج" in question:
                response = f"📦 المنتج الأكثر مبيعًا: {row['المنتج الأكثر مبيعًا']}"

            st.success(response)
