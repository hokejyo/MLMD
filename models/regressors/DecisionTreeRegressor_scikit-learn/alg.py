import streamlit as st

# Define possible modelsd in a dict
# Format of the dict: model name -> model code

MODEL = {
    "model": "DecisionTreeRegressor",
}

# LightGBM can use -- categorical features -- as input directly. It doesn’t need to convert 
# to one-hot encoding, and is much faster than one-hot encoding (about 8x speed-up).

def show():
    """Shows the components for the template and returns user inputs as dict."""
    
    # `show()` is the only method required in this module. You can add any other code 
    # you like above or below. 
    
    inputs = {}  # dict to store all user inputs until return
    
    # with st.sidebar:
        
    # Render all template-specific sidebar components here. 

    # Use ## to denote sections. Common sections for training templates: 
    # Model, Input data, Preprocessing, Training, Visualizations
    # Store all user inputs in the `inputs` dict. This will be passed to the code
    # template later.
    inputs["model"] = MODEL["model"]
    
    # st.write("preprocessing")
    # inputs["Normalize"] = st.selectbox('normalize method', ['Z-Score Standardization','Min-Max Scale'])
    
    st.info('TO SOLVE **REGRESSION**')
    
    # st.write('training')

    # st.write("No additional parameters")
    col1, col2 = st.columns([2,2])
    with col1:
        with st.expander("Hyper Parameter"):
            inputs['criterion'] = st.selectbox('criterion',('squared_error','friedman_mse','absolute_error','poisson'))
            inputs['splitter'] = st.selectbox('splitter',('best','random'))
            max_depth = st.checkbox('max depth', None)
            inputs['max depth'] = None
            if max_depth:
                inputs['max depth'] = st.number_input('max depth',1, 10000, 3)
            inputs['min samples leaf'] = st.number_input('min samples leaf', 1, 1000, 1)
            inputs['min samples split'] = st.number_input('min samples split', 2, 1000, 2)

            random_state = st.checkbox('random state 1024',True)
            if random_state:
                inputs['random state'] = 1024
            else:
                inputs['random state'] = None
             
        # graph parameter
        with st.expander("Tree Graph"):
            inputs['tree graph'] = st.checkbox('tree graph', False)
            if inputs['tree graph']:
                inputs['filled'] = st.selectbox('filled',('True','False'))
                inputs['rounded'] = st.selectbox('rounded',('True','False'))

    return inputs,col2


# To test the alg independent of the app or template, just run 
# `streamlit run alg.py` from within this folder.
if __name__ == "__main__":
    show()
    
    