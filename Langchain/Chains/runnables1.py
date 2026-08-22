from abc import ABC, abstractmethod
import random

class Runnable(ABC):
    @abstractmethod
    def invoke(input_data):
        pass

class LLM(Runnable):
    def __init(self):
        print("LLM created....")
    def invoke(self,prompt):
        responses_list = [
            "Delhi is the capital of India",
            "IPL is a cricket league",
            "AI stands for Artificial intelligence"
        ]
        return  {'response':random.choice(responses_list)}
    def predict(self,prompt):
        return "Call invoke instead of predict method"
    
class PromptTemplate(Runnable):
    def __init__(self,template,input_variables):
        self.template = template
        self.input_variables = input_variables
    def invoke(self,input_dict):
        return self.template.format(**input_dict)
    def format(self, input_dict):
        return "Use invoke instead of format"
    
class RunnableConnector(Runnable):
    def __init__(self,runnable_list):
        self.runnable_list = runnable_list
    def invoke(self,input_data):
        for runnable in self.runnable_list:
            input_data=runnable.invoke(input_data)
        return input_data
class Stroutputparaser(Runnable):
    def __init__(self):
        pass
    def invoke(self,input_data):
        return input_data['response']

llm = LLM()
parser  =Stroutputparaser()
template = PromptTemplate(template ='write a {length} poem about {topic}',input_variables=['length','topic'])
chain = RunnableConnector([template,llm,parser])
result = chain.invoke({'length':'long','topic':'India'})

print(result)

template1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="Explain the following joke {response}",
    input_variables=['response']
)

chain1 = RunnableConnector([template1,llm])
chain1.invoke({'topic':'AI'})

chain2 =RunnableConnector([template2,llm,parser])
chain2.invoke({'response':'This is a joke'})

final_chain = RunnableConnector([chain1,chain2])
res = final_chain.invoke({'topic':'Cricket'})
print(res)