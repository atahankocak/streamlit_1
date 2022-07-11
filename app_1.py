def streamlit_run():
    
    import streamlit as st

    header = st.container()
    dataset = st.container()
    features = st.container()
    model = st.container()

    shap = st.container()

    with header:
        st.title("Hello World!")
        st.text("\n some dddddddddddddddddddddddddddddddddddddddddddddd goes here")

    with dataset:
        st.header('No data yet, just testing this guy')

    with features:
        st.header("features, only only only the good engineered ones")

    with model:
        st.text("model result pops here")

    with shap:
        st.text("shap force plot goes here")


if __name__ == "__main__":
    streamlit_run()