import streamlit as st
from streamlit.logger import get_logger

from server.file_handlers import save_db_dump

LOGGER = get_logger(__name__)

def run() -> None:
    st.markdown("""
                ## Upload File Below.

                Make sure it is a dump of the 
                database *db8sqnszgozxhp* with 
                the `rms` tag

                Upload the file as a .zip format
                This can be specified in the sql 
                dump tag

                ### More info to be added.

                """)
    

    uploaded_file = st.file_uploader("## Upload Database Dump")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        save_db_dump(bytes_data)
    

if __name__ == "__main__":
    run()
