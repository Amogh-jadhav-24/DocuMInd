from langchain_core.prompts import PromptTemplate


from langchain_core.output_parsers import StrOutputParser



def create_chain(llm):


    prompt = PromptTemplate(

template="""

Answer the question using only the context.


Context:
{context}


Question:
{question}


Answer:

""",

input_variables=[
"context",
"question"
]

)



    chain = (

        prompt

        |

        llm

        |

        StrOutputParser()

    )


    return chain