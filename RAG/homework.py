from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
import os
from fastapi import FastAPI
from pydantic import BaseModel


load_dotenv()

app = FastAPI()

client = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY")
)
#print(os.getenv("OPENAI_API_KEY"))
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a question paper generator.{format}."),
        (
            "user", "Create a question paper on topic {topic} of total marks {totalMarks} {questionType} type questions and marks per question is {marksPerQuestion}"
        )
    ]
)



Question = []

class Questionpaper(BaseModel):
    topic: str
    totalMarks: int
    questionType: str
    marksPerQuestion: int

class Que(BaseModel):
    Ques : str
    Options : list[str]
    answer : str

class Structure(BaseModel):
    topic : str
    passing_marks : int
    questions : list[Que]


@app.post("/questionpaperGenerator/")
def que_paper(question: Questionpaper):

    parser = PydanticOutputParser(pydantic_object=Structure)
    chain = prompt | client | parser 


    response = chain.invoke(
        {
            "topic": question.topic,
            "totalMarks": question.totalMarks,
            "questionType": question.questionType,
            "marksPerQuestion": question.marksPerQuestion,
            "format" : parser.get_format_instructions()
        
        }
    )

    Question.append(response)

    return {
        "msg": "Question paper generated successfully",
        "question_paper": response
    }