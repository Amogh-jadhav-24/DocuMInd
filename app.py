# # import streamlit as st


# # from document_loader import load_document

# # from text_splitter import split_documents

# # from embedding import get_embeddings

# # from vector_store import create_vector_store

# # from llm import get_llm

# # from rag_chain import create_chain



# # st.title(
# # "Gemini Document Q&A"
# # )


# # uploaded_file = st.file_uploader(
# # "Upload PDF",
# # type="pdf"
# # )



# # if uploaded_file:


# #     file_path = (
# #         "data/"
# #         +
# #         uploaded_file.name
# #     )


# #     with open(
# #         file_path,
# #         "wb"
# #     ) as f:


# #         f.write(
# #             uploaded_file.read()
# #         )



# #     documents = load_document(
# #         file_path
# #     )


# #     chunks = split_documents(
# #         documents
# #     )


# #     embeddings = get_embeddings()


# #     vector_db = create_vector_store(

# #         chunks,

# #         embeddings
# #     )



# #     question = st.text_input(
# #         "Ask question"
# #     )



# #     if question:


# #         retriever = vector_db.as_retriever()


# #         docs = retriever.invoke(
# #             question
# #         )


# #         context = "\n".join(

# #             [
# #             d.page_content
# #             for d in docs
# #             ]

# #         )


# #         llm = get_llm()


# #         chain = create_chain(
# #             llm
# #         )


# #         answer = chain.invoke(

# #             {

# #             "context":context,

# #             "question":question

# #             }

# #         )


# #         st.write(answer)

# #-------------------------------------------------------------------------------------------

# import streamlit as st
# import os


# from document_loader import load_document
# from text_splitter import split_documents
# from embedding import get_embeddings
# from vector_store import create_vector_store
# from llm import get_llm
# from rag_chain import create_chain




# # ---------------- PAGE CONFIG ---------------- #

# st.set_page_config(
#     page_title="Page Pilot - AI Document Chat",
#     page_icon="📄",
#     layout="wide"
# )



# # ---------------- CSS ---------------- #

# st.markdown(
    
#     """
#     <style>


#     .stApp {

#         background: linear-gradient(
#             135deg,
#             #0f172a,
#             #020617
#         );

#         color:white;

#     }


#     h1 {

#         text-align:center;
#         color:#38bdf8;
#         font-size:55px;

#     }



#     .subtitle {

#         text-align:center;
#         color:#cbd5e1;
#         font-size:20px;
#         margin-bottom:40px;

#     }




#     div[data-testid="stFileUploader"] {

#         background:#1e293b;
#         padding:30px;
#         border-radius:20px;
#         border:2px dashed #38bdf8;

#     }



#     .stTextInput input {

#         background:#1e293b;
#         color:white;
#         border-radius:15px;
#         padding:15px;

#     }




#     .answer-box {

#         background:#1e293b;
#         padding:25px;
#         border-radius:20px;
#         margin-top:30px;
#         color:white;
#         font-size:18px;
#         border-left:5px solid #38bdf8;

#     }



#     .success {

#         background:#064e3b;
#         padding:15px;
#         border-radius:10px;

#     }


#     </style>
#     """,

#     unsafe_allow_html=True
# )





# # ---------------- HEADER ---------------- #

# st.markdown(
#     """

# <h1>📄 Gemini Document AI</h1>


# <p class="subtitle">

# Upload your PDF and ask questions using Gemini RAG

# </p>


# """,

# unsafe_allow_html=True
# )





# # ---------------- CREATE DATA FOLDER ---------------- #

# os.makedirs(
#     "data",
#     exist_ok=True
# )





# # ---------------- FILE UPLOAD ---------------- #

# uploaded_file = st.file_uploader(

#     "Upload Your PDF",

#     type="pdf"

# )






# if uploaded_file:


#     file_path = os.path.join(

#         "data",

#         uploaded_file.name

#     )



#     with open(

#         file_path,

#         "wb"

#     ) as f:


#         f.write(

#             uploaded_file.getbuffer()

#         )




#     st.success(

#         "Document Uploaded Successfully"

#     )





#     with st.spinner(

#         "Reading Document..."

#     ):


#         documents = load_document(

#             file_path

#         )





#     with st.spinner(

#         "Splitting Document..."

#     ):


#         chunks = split_documents(

#             documents

#         )






#     with st.spinner(

#         "Creating Embeddings..."

#     ):


#         embeddings = get_embeddings()



#         vector_db = create_vector_store(

#             chunks,

#             embeddings

#         )





#     st.success(

#         "AI is ready. Ask your questions!"

#     )






#     # ---------------- QUESTION ---------------- #

#     question = st.text_input(

#         "Ask anything about your document"

#     )






#     if question:


#         with st.spinner(

#             "Thinking..."

#         ):


#             retriever = (

#                 vector_db.as_retriever()

#             )



#             related_docs = (

#                 retriever.invoke(

#                     question

#                 )

#             )





#             context = "\n".join(

#                 [

#                     doc.page_content

#                     for doc in related_docs

#                 ]

#             )





#             llm = get_llm()



#             chain = create_chain(

#                 llm

#             )





#             answer = chain.invoke(

#                 {

#                     "context": context,


#                     "question": question

#                 }

#             )






#         # ---------------- ANSWER UI ---------------- #

#         st.markdown(

#             f"""

#             <div class="answer-box">


#             <h3>🤖 Gemini Answer</h3>


#             {answer}


#             </div>


#             """,


#             unsafe_allow_html=True

#         )



# else:


#     st.info(

#         "Upload a PDF document to start chatting"

#     )

# #-------------------------------------------------------------------------------------------

import streamlit as st
import os

from document_loader import load_document
from text_splitter import split_documents
from embedding import get_embeddings
from vector_store import create_vector_store
from llm import get_llm
from rag_chain import create_chain


# ================= PAGE CONFIG ================= #

st.set_page_config(
    page_title="DocuMind AI",
    page_icon="📄",
    layout="centered"
)



# ================= CSS ================= #

st.markdown(
"""
<style>


/* Background */
.stApp {

    background:#FAFAFA;

}


/* Hide Streamlit Menu */
#MainMenu {
    visibility:hidden;
}

footer {
    visibility:hidden;
}



/* Header */

.main-title {

    text-align:center;
    font-size:46px;
    font-weight:800;
    color:#111111;
    margin-top:20px;

}


.highlight {

    color:#DE7356;

}


.subtitle {

    text-align:center;
    color:#555;
    font-size:18px;
    margin-bottom:40px;

}



/* Upload Card */

div[data-testid="stFileUploader"] {

    background:white;

    padding:25px;

    border-radius:18px;

    border:1.5px solid #eeeeee;

    box-shadow:
    0 8px 25px rgba(0,0,0,0.06);

}



div[data-testid="stFileUploader"]:hover {

    border-color:#DE7356;

}




/* Input */

.stTextInput input {


    background:white;

    border-radius:14px;

    border:1px solid #ddd;

    padding:14px;

    color:#111;

}



.stTextInput input:focus {

    border:1px solid #DE7356;

}





/* Answer Box */

.answer-card {


    background:white;

    margin-top:25px;

    padding:25px;

    border-radius:18px;


    border-left:5px solid #DE7356;


    box-shadow:
    0 8px 25px rgba(0,0,0,0.08);


    color:#222;

    line-height:1.7;

}



.answer-title {


    color:#DE7356;

    font-weight:700;

    font-size:22px;

    margin-bottom:10px;


}





/* Alerts */

div[data-testid="stAlert"] {

    border-radius:12px;

}



</style>
""",

unsafe_allow_html=True
)



# ================= HEADER ================= #

st.markdown(
"""

<div class="main-title">

Docu<span class="highlight">Mind</span> AI

</div>


<div class="subtitle">

Chat with your documents using DocuMind AI

</div>


""",

unsafe_allow_html=True
)





# ================= CREATE FOLDER ================= #

os.makedirs(
    "data",
    exist_ok=True
)





# ================= FILE UPLOAD ================= #

uploaded_file = st.file_uploader(

    "Upload PDF Document",

    type="pdf"

)




if uploaded_file:


    file_path = os.path.join(

        "data",

        uploaded_file.name

    )



    with open(file_path,"wb") as f:


        f.write(

            uploaded_file.getbuffer()

        )




    st.success(

        "Document uploaded successfully"

    )





    with st.spinner(
        "Reading document..."
    ):


        documents = load_document(

            file_path

        )




    with st.spinner(
        "Processing document..."
    ):


        chunks = split_documents(

            documents

        )





    with st.spinner(
        "Creating knowledge base..."
    ):


        embeddings = get_embeddings()



        vector_db=create_vector_store(

            chunks,

            embeddings

        )






    question = st.text_input(

        "Ask your question"

    )





    if question:


        with st.spinner(

            "Finding answer..."

        ):



            retriever = vector_db.as_retriever()



            related_docs = retriever.invoke(

                question

            )





            context="\n".join(

                [

                    doc.page_content

                    for doc in related_docs

                ]

            )





            llm=get_llm()



            chain=create_chain(

                llm

            )





            answer=chain.invoke(

                {

                    "context":context,

                    "question":question

                }

            )






        st.markdown(

            f"""

<div class="answer-card">


<div class="answer-title">

🤖 Answer

</div>


{answer}


</div>


""",

unsafe_allow_html=True

        )





else:


    st.info(

        "Upload a PDF to start chatting"

    )
