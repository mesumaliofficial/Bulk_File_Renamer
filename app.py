import io
import zipfile
import streamlit as st

st.set_page_config(page_title="📂 Bulk File Renamer", layout="wide")

st.title("📂 Bulk File Renamer")
st.text("Upload your file and rename your all files.")

upload_files = st.file_uploader("Upload Multiple Files", accept_multiple_files=True)
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    name_pattern = st.text_input("Enter name (use `{n}` for numbering):", "files_{n}")
with col2:
    start_index = st.number_input("Starting Number", min_value=0, value=0)
with col3:
    file_extension = st.text_input("File Extension (eg .jpg, .png)")

if st.button("Rename Files"):
    if upload_files and name_pattern and file_extension:
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zipf:
            for i, uploaded_files in enumerate(upload_files):
                new_name = name_pattern.format(n=start_index + i) + file_extension
                zipf.writestr(new_name, uploaded_files.read())
        st.success(f"Files renamed and saved in {name_pattern}.zip")
        st.download_button(
            label="Download Renamed Files",
            data=zip_buffer,
            file_name=f"{name_pattern}.zip",
            mime="application/zip"
        )
    else:
        st.error("Please fill in all fields and upload files.")