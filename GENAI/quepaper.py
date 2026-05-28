from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser , JsonOutputParser,PydanticOutputParser

import os

load_dotenv()

app = FastAPI()

client = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY")
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a Question paper Generator.  {format} "),
        (
            "user",
            """""
            Create a question paper.

            Topic: {topic}
            Total Marks: {totalmarks}
            Question Type: {questionType}
            Marks Per Question: {marksPerQuestion}

            Generate proper questions.
            """
        )
    ]
)






class QuestionPaperBody(BaseModel):
    topic:str
    totalmarks: int
    questionType : str
    marksPerQuestion : int



class Question(BaseModel):
    Ques:str
    Options:list[str]
    answer: str

class QuestionPaper(BaseModel):
    topic :str
    passing_marks : int
    questions : list[Question]



parser = PydanticOutputParser(pydantic_object=QuestionPaper)
chain = prompt | client | parser




@app.post("/questionpaperGenerator/")
def create_questionpaper(questionPaper:QuestionPaperBody):
    response = chain.invoke(
        {
            "topic": questionPaper.topic,
            "totalmarks": questionPaper.totalmarks,
            "questionType": questionPaper.questionType,
            "marksPerQuestion": questionPaper.marksPerQuestion,
            "format": parser.get_format_instructions()
        }
    )
    print("QuestionPaper")
    print(response)

    return{
        "topic": questionPaper.topic,
        "questiontype":questionPaper.questionType,
        "QuestionPaper": response
    }


# @app.get("/questionpaperSee/")
# def get_questionpaper():
#     return{
#         "msg":"question paper  data retrieved successfully",
#         "data": qp
     
#     }