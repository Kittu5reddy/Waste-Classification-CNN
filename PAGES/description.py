import streamlit as st

st.write("""
Project: Waste Classification using Convolutional Neural Network (CNN)

Description:
This Streamlit application utilizes a pre-trained Convolutional Neural Network (CNN) based on the VGG16 architecture to classify waste images into four categories: **Biodegradable, Non-Biodegradable, Trash, or Hazardous**. 

The primary objective of this project is to assist in waste management by automating waste classification, enabling better sorting and recycling processes.

Features:
1. **Model Loading**: The model is loaded using a cached function to enhance performance and reduce redundant computations.
2. **Image Upload**: Users can upload waste images in JPG, JPEG, or PNG formats.
3. **Prediction**: The uploaded image is processed and classified into one of the four waste categories using the trained CNN model.
4. **User Feedback**: The application provides visual feedback by displaying the uploaded image and showing the predicted classification result.
5. **Preprocessing**: The image undergoes resizing, normalization, and tensor conversion before being fed into the model.

Model Details:
- The model is based on the **VGG16 architecture** with a modified classifier layer for four output classes.
- The model is pre-trained but fine-tuned to recognize waste categories using a dataset from Kaggle.
- The model file (`model.pth`) is loaded during runtime for inference.

Usage:
- Run the application with Streamlit.
- Upload an image of waste.
- The model predicts and displays the waste classification result.

Dependencies:
`altair==5.5.0`
`attrs==25.1.0`
`blinker==1.9.0`
`cachetools==5.5.1`
`certifi==2025.1.31`
`charset-normalizer==3.4.1`
`click==8.1.8`
`filelock==3.17.0`
`fsspec==2025.2.0`
`gitdb==4.0.12`
`GitPython==3.1.44`
`idna==3.10`
`Jinja2==3.1.5`
`jsonschema==4.23.0`
`jsonschema-specifications==2024.10.1`
`markdown-it-py==3.0.0`
`MarkupSafe==3.0.2`
`mdurl==0.1.2`
`mpmath==1.3.0`
`narwhals==1.26.0`
`networkx==3.4.2`
`numpy==2.2.3`
`packaging==24.2`
`pandas==2.2.3`
`pillow==11.1.0`
`protobuf==5.29.3`
`pyarrow==19.0.0`
`pydeck==0.9.1`
`Pygments==2.19.1`
`python-dateutil==2.9.0.post0`
`pytz==2025.1`
`referencing==0.36.2`
`requests==2.32.3`
`rich==13.9.4`
`rpds-py==0.22.3`
`six==1.17.0`
`smmap==5.0.2`
`streamlit==1.42.0`
`sympy==1.13.1`
`tenacity==9.0.0`
`toml==0.10.2`
`torch==2.6.0`
`torchvision==0.21.0`
`tornado==6.4.2`
`typing_extensions==4.12.2`
`tzdata==2025.1`
`urllib3==2.3.0`
`watchdog==6.0.0`
"""
)