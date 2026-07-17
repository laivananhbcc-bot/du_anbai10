import streamlit as st
st.title('Nhà hàng lego')
khai_vi = ['Bánh nướng','Súp','Salad','Goi','Bánh mì bơ']
chinh = ['pizza','pad thai','steak','Mousaaka']
trang_mieng = ['cheesecake','tiramisu','creme brulee','panna cotta']
with st.form('Thuc don yeu thich:'):
    op1 = st.multiselect('Món khai vị:',khai_vi)
    op2 = st.multiselect('Món chính:',chinh)
    op3 = st.multiselect('Mon trang mieng:',trang_mieng)
    submit = st.form_submit_button('Xac nhan!')
if submit:
    st.write('Cac lua chon cua ban la:')
    st.write('Mon khai vi:')
    if len(op1) ==0: st.write('Ban chua chon mon Khai vi!')
    else:
        for x in op1: st.write(x)
    st.write('Mon chinh:')
    if len(op2) == 0:
        st.write('Ban chua chon mon Chinh!')
    else:
        for x in op2: st.write(x)
    st.write('Mon trang mieng:')
    if len(op3) == 0:
        st.write('Ban chua chon mon trang mieng!')
    else:
        for x in op3: st.write(x)
