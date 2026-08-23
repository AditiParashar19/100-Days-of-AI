from langchain_community.document_loaders import WebBaseLoader

url="https://www.flipkart.com/wearable-smart-devices/wearable-accessories/pr?sid=ajy,vne&marketplace=FLIPKART"
loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))
print(docs[0].page_content)

# we can also pass a list of urls
#we can also ask questions from it