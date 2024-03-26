import streamlit as st
#title
st.set_page_config(page_title="my webpage",page_icon=":tada:",layout="wide")
with st.container():
    st.subheader("hi,i am surya :wave:")
    st.title("a data analyst from india")
    st.write("python web")



with st.container():
    st.write("---")
    left_column, right_column=st.columns(2)
    with left_column:
        st.header("what I do")
        st.write("##")
        st.write(
        """python coding:
        -java,
        -javascript.,
        -c,
        -c#,
        """
        )



