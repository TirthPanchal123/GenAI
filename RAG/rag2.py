from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser , PydanticOutputParser
from pydantic import BaseModel


load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo")

class Question(BaseModel):
    question: str
    options : list[str]
    answer : str

class QuestionPaper (BaseModel):
    topic : str
    passing_score : int
    questions: list[Question]

prompt =ChatPromptTemplate.from_messages(
    [
        ("system","you are a question paper generator. {format}."),
        ("user","generate a ques paper for topic {topic} with question of type {question_type} and number of questions {num_questions}")
    ]
)

parser = PydanticOutputParser(pydantic_object=QuestionPaper)


chain = prompt | llm | parser

response = chain.invoke({
    "topic":"physics",
    "question_type":"mcq",
    "num_questions":"5",
    "format":parser.get_format_instructions()
})

print(response)