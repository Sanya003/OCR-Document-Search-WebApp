import streamlit as st
from PIL import Image
import pytesseract
import re

def highlight_text(text, keyword):
    escaped_key = re.escape(keyword)
    highlighted_text = re.sub(f'({escaped_key})', r'<mark>\1</mark>', text, flags = re.IGNORECASE)
    return highlighted_text

st.title('OCR Document Search Web App')
st.divider()

_ = '''
def got_ocr(image_path):
    from transformers import AutoModel, AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained("stepfun-ai/GOT-OCR2_0", trust_remote_code=True)
    model = AutoModel.from_pretrained("stepfun-ai/GOT-OCR2_0", trust_remote_code=True, low_cpu_mem_usage=True, device_map='cuda', use_safetensors=True, pad_token_id=tokenizer.eos_token_id)
    model=model.eval().cuda()
    image = Image.open(image_path)
    res = model.chat(tokenizer, image, ocr_type='ocr')
    return res
'''

uploaded_img = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'])

if uploaded_img is not None:
    image = Image.open(uploaded_img)

    st.image(image, caption='Uploaded image', use_column_width=True)

    extracted_text = pytesseract.image_to_string(image, lang='eng+hin')

    st.subheader('Extracted text')
    st.divider()

    st.text(extracted_text)

    st.divider()

    search_query = st.text_input('Enter a keyword to search in the extracted text - ')

    if search_query:

        highlighted_text = highlight_text(extracted_text, search_query)

        st.subheader('Text with Highlighted Keyword')
        st.markdown(highlighted_text, unsafe_allow_html=True)
