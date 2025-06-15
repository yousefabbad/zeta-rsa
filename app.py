import streamlit as st
from sympy import factorint
import numpy as np

# واجهة المستخدم
st.set_page_config(page_title="تحليل جودة المفاتيح - Zeta x RSA", layout="centered")
st.title("🔐 تحليل جودة مفاتيح RSA باستخدام أصفار زيتا")
st.markdown("هذه الأداة تقارن بين الفروقات في عوامل المفتاح وبين أصفار دالة زيتا لرصد النمط الرياضي.")

# إدخال المستخدم
modulus_input = st.text_input("🧮 أدخل قيمة modulus (عدد صحيح كبير):")

# أصفار زيتا المعروفة (أول 20 صفر غير تافه)
zeta_zeros = [
    14.134725, 21.022040, 25.010857, 30.424876, 32.935061,
    37.586178, 40.918719, 43.327073, 48.005150, 49.773832,
    52.970321, 56.446248, 59.347044, 60.831780, 65.112544,
    67.079811, 69.546401, 72.067158, 75.704690, 77.144840
]

# عند الضغط على زر التحليل
if st.button("🔍 تحليل"):
    if not modulus_input.isdigit():
        st.error("يرجى إدخال عدد صحيح فقط.")
    else:
        modulus = int(modulus_input)
        factors = factorint(modulus)
        factor_keys = sorted(factors.keys())
        factor_diffs = np.diff(factor_keys) if len(factor_keys) > 1 else []

        st.subheader("📊 تحليل الفروقات:")
        if len(factor_diffs) > 0:
            zeta_diffs = np.diff(zeta_zeros)
            for i in range(min(len(factor_diffs), len(zeta_diffs))):
                st.write(f"الفرق رقم {i+1}: عامل RSA = {factor_diffs[i]} ⬄ زيتا = {zeta_diffs[i]:.6f}")
        else:
            st.info("المفتاح يحتوي على عامل أولي واحد فقط. لا يمكن حساب الفروقات.")
        
        st.subheader("📌 العوامل:")
        for k, v in factors.items():
            st.write(f"{k} ^ {v}")
