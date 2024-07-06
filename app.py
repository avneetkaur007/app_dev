import streamlit as st
st.title("Loan approval app")
st.write('This app will help you')
st.header('kindly enter the details')
st.text_input('Name')
c=st.number_input('enter your Credit score')
if c>500:
    st.write('yes sir,congratulations')
    #st.balloons()
    x=st.radio('What type of loan ?',options=['Home loan','Car loan','Personal loan'])
    if x=='Home loan':
        s=st.number_input('enter ur salary')
        y=st.checkbox('Are you looking for loan for more than 20 yrs')
        st.write('Ok sir,our executive will contact you')

else:
    st.write('Sorry sir')

