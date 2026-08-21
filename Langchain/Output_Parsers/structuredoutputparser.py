from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# create schema 
schema = [
    ResponseSchema(name='fact_1',description="fact 1 about the topic"),
    ResponseSchema(name='fact_2',description="fact 2 about the topic"),
    ResponseSchema(name='fact_3',description="fact 3 about the topic")
]

#create parser
parser = StructuredOutputParser.from_response_schemas(schema)

template =PromptTemplate(
    template="Give 3 facts about {topic}\n {format_instruction}",
    input_varibles=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# prompt = template.invoke({'topic':'black hole'})

# res  =model.invoke(prompt)

# final_result = parser.parse(res.content)
chain = template | model |parser

final_result =chain.invoke({
    'topic':'black hole'
})

print(final_result)

