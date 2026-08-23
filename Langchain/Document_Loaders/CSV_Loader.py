from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="C:\Langchain-CampusX\Crop_recommendation.csv")

data = loader.load()
print(data[0])
print(len(data))
#python.langchain.com/docs/integration/document_loaders/#pdf