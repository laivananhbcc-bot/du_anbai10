import streamlit as st
st.title('Chào mừng đến với tiệm trà sữa Mixue')
st.write('Mời chọn thực đơn')
with st.form('Đồ uống'):
    drink = ('Truyen thong','Matcha','Socola')
    opt_d = st.selectbox('Chọn đồ uống:',drink)
    sugars = ('Trắng','Nâu','Không đường')
    opt_s = st.selectbox('Chọn đường:',sugars)
    topping = ('Trân châu đen','Trân châu trắng','Rau cau')
    opt_t = st.selectbox('Chọn thạch:',topping)
    slg = st.slider('Số lượng:',1,20,1)
    bill = {
        'Loại do uong': opt_d,
        'Loại duong': opt_s,
        'Loại thach': opt_t,
        'So luong': slg
    }
    if st.form_submit_button('Xác nhận'):
        st.write('Ban da chon:')
        for x, y in bill.items():
            st.write(f'- {x}: {y}')
