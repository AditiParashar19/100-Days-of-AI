from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
loader = DirectoryLoader(
    path="C:\Langchain-CampusX\PDF_FOLDER",
    glob='*.pdf',  #all files pdf
    loader_cls=PyPDFLoader 
)

docs = loader.lazy_load()
# print(docs)
# print(len(docs))
# print(docs[0].page_content)
# print(docs[0].metadata)
# print(docs[14].page_content)

for document in docs:
    print(document.metadata)

#lazy_load = in memory one page comes in memory then erase then 2 comes and erase and goes on