
import streamlit as st
import fitz

# Page configuration
st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="wide"
)

# Application heading
st.title("📚 StudyMate AI")
st.subheader("Your Personal AI Study Assistant")

st.write("Upload your PDF notes and study smarter!")

# PDF uploader
uploaded_file = st.file_uploader(
    "Choose your PDF file",
    type=["pdf"]
)

if uploaded_file is not None:

    pdf = fitz.open(
        stream=uploaded_file.getvalue(),
        filetype="pdf"
    )

    extracted_text = ""

    for page_number, page in enumerate(pdf):

        text = page.get_text()

        extracted_text += (
            f"\n--- Page {page_number + 1} ---\n"
            + text
        )

    st.success("PDF uploaded successfully!")

    st.write("Total pages:", len(pdf))

    st.subheader("Extracted Text")

    if extracted_text.strip():

        st.text_area(
            "Your PDF Content",
            extracted_text,
            height=350
        )

        st.download_button(
            "Download Extracted Text",
            extracted_text,
            file_name="study_notes.txt"
        )

    else:
        st.warning("No readable text found in this PDF.")
