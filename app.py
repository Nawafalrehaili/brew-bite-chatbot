
import streamlit as st
import pandas as pd

# تحميل البيانات
@st.cache_data
def load_data():
    return pd.read_csv("brew_bite_branches_arabic.csv")

df = load_data()

# عنوان التطبيق
st.title("شات بوت فروع Brew & Bite")

# إدخال سؤال المستخدم
question = st.text_input("اكتب سؤالك:")

if question:
    branch_name = None
    for word in ["جدة", "الرياض", "الدمام", "الخبر"]:
        if word in question:
            branch_name = word
            break

    if branch_name:
        row = df[df["المدينة"].str.contains(branch_name, na=False)]
        if not row.empty:
            row = row.iloc[0]
            if "دخل" in question:
                st.success(f"💰 الدخل الشهري للفرع هو: {row['الدخل الشهري']} ريال")
            elif "مدير" in question:
                st.success(f"🧑‍💼 مدير الفرع: {row['اسم المدير']}")
            elif "رضا" in question:
                st.success(f"📊 نسبة رضا العملاء: {row['رضا العملاء']}")
            else:
                st.info("❓ يرجى تحديد نوع المعلومة المطلوبة (دخل، مدير، رضا، ...)")
        else:
            st.error("❌ لم يتم العثور على الفرع المطلوب.")
    else:
        st.warning("⚠️ يرجى تحديد المدينة في سؤالك.")
