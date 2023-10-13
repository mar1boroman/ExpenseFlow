import redis
import os
import streamlit as st
import openai
import numpy as np
from dotenv import load_dotenv
from streamlit_extras.colored_header import colored_header
from rich import print
from streamlit_extras.app_logo import add_logo
from redisvl.query import VectorQuery
from redisvl.index import SearchIndex

load_dotenv()
OPENAI_EMBEDDING_MODEL = "text-embedding-ada-002"
INDEX_NAME = "idx:blogs"
EXPLANATION = []
# Common Functions


def get_embedding(doc):
    EXPLANATION.append(
        f"The app uses the Open AI *{OPENAI_EMBEDDING_MODEL}* API to generate an embedding for the text '{doc}'"
    )
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Embedding.create(
        input=doc, model=OPENAI_EMBEDDING_MODEL, encoding_format="float"
    )
    embedding = response["data"][0]["embedding"]
    return embedding


def find_category(narration):
    vector = get_embedding(narration)
    query = VectorQuery(
        vector=vector,
        vector_field_name="Narration_Embedding",
        return_fields=["Category", "Narration", "vector_distance"],
        num_results=1,
    )
    index = SearchIndex.from_existing("idx:txn", "redis://localhost:6379")
    result = index.query(query)[0]
    vector_score = round(1 - float(result['vector_distance']), 2)
    print(vector_score)
    return result


def get_explanation():
    expl_doc = ""
    for i, txt in enumerate(EXPLANATION):
        expl_doc += f"{i+1} : {txt}<br><br>"
    return expl_doc


def main():
    st.set_page_config()
    add_logo("assets/redis-favicon-144x144.png")
    colored_header(
        label="Find Category",
        description="Use Vector Similarity search categorize transactions based on pre-labelled transactions",
        color_name="violet-60",
    )
    form = st.form(key="search_form")
    prompt = form.text_input(label="Enter some text")
    submit = form.form_submit_button(label="Submit")

    if submit:
        result = find_category(narration=prompt)
        st.header(result['Category'])
        st.markdown(f"""
        Matched with existing : {result['Narration']}
        <br>
        Vector score : {round(1 - float(result['vector_distance']), 2)}
        """, unsafe_allow_html=True)

    with form.expander(label="Execution Log"):
        st.markdown(get_explanation(), unsafe_allow_html=True)


if __name__ == "__main__":
    main()
