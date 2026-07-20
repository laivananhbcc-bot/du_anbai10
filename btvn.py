import streamlit as st
st.title('Thuc don hang ngay')
bua_sang = ['Bánh nướng','Pho','Salad','Goi','Bánh mì bơ']
bua_trua = ['pizza','pad thai','steak','Mousaaka']
bua_toi = ['cheesecake','tiramisu','creme brulee','panna cotta']
with st.form('Thuc don yeu thich:'):
    op1 = st.multiselect('Món bua sang:',bua_sang)
    op2 = st.multiselect('Món bua trua:',bua_trua)
    op3 = st.multiselect('Mon bua toi:',bua_toi)
    submit = st.form_submit_button('Xac nhan!')
if submit:
    st.write('Cac lua chon cua ban la:')
    st.write('bua sang:')
    if len(op1) ==0: st.write('Ban chua chon bua sang!')
    else:
        for x in op1: st.write(x)
    st.write('bua trua:')
    if len(op2) == 0:
        st.write('Ban chua chon bua trua!')
    else:
        for x in op2: st.write(x)
    st.write('bua toi:')
    if len(op3) == 0:
        st.write('Ban chua chon bua toi!')
    else:
        for x in op3: st.write(x)
