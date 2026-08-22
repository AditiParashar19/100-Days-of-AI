import random
class LLM:
    def __init(self):
        print("LLM created....")
    def predict(self,prompt):
        responses_list = [
            "Delhi is the capital of India",
            "IPL is a cricket league",
            "AI stands for Artificial intelligence"
        ]
        return  {'response':random.choice(responses_list)}
    
llm = LLM()
answer= llm.predict("What is the capital of India?")

print(answer)


class PromptTemplate:
    def __init__(self,template,input_variables):
        self.template = template
        self.input_variables = input_variables
    def format(self, input_dict):
        return self.template.format(**input_dict)

template = PromptTemplate(template ='write a {length} poem about {topic}',input_variables=['length','topic'])
temp = template.format({'topic':'India','length':'short'})

print(temp)

llm = LLM()
res = llm.predict(temp)
print(res)

class  Chain:
    def __init__(self,llm,prompt):
        self.llm= llm
        self.prompt = prompt
    def run(self,input_dict):
        final_prompt = self.prompt.format(input_dict)
        result = self.llm.predict(final_prompt)
        return result['response']

chain = Chain(llm,template)
output = chain.run({'length':'short','topic':"India"})
print(output)




