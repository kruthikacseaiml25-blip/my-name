import streamlit as st
from PIL import Image
import io

# Page settings
st.set_page_config(
    page_title="Image to PDF Scanner",
    page_icon="📄"
)

# Title
st.title("📄 Image to PDF Scanner")
st.write("Upload an image, convert it to grayscale, and download it as a PDF.")

# File uploader
uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["png", "jpg", "jpeg"]
)

# Check if file is uploaded
if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file)

    # Display original image
    st.image(
        image,
        caption="Original Image",
        use_container_width=True
    )

    # Convert button
    if st.button("Convert to Grayscale & PDF"):

        # Convert image to grayscale then RGB
        gray_image = image.convert("L").convert("RGB")

        # Show grayscale image
        st.image(
            gray_image,
            caption="Grayscale Image",
            use_container_width=True
        )

        # Save PDF into memory
        pdf_bytes = io.BytesIO()
        gray_image.save(pdf_bytes, format="PDF")
        pdf_bytes.seek(0)

        # Download button
        st.download_button(
            label="📥 Download PDF",
            data=pdf_bytes,
            file_name="document.pdf",
            mime="application/pdf"
        )