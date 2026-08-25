from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """Artificial Intelligence (AI) is transforming industries across the world by enabling machines to perform tasks that traditionally required human intelligence. AI systems can analyze large amounts of data, recognize patterns, make predictions, and automate repetitive tasks. From healthcare and education to finance and transportation, AI is improving efficiency and creating new opportunities.
Machine Learning (ML) is a subset of AI that allows computers to learn from data without being explicitly programmed. ML algorithms identify patterns in historical data and use those patterns to make predictions or decisions. Common applications include spam email detection, recommendation systems, fraud detection, and image recognition.
Deep Learning is a specialized branch of Machine Learning that uses artificial neural networks with multiple layers to model complex relationships in data. Deep learning has achieved remarkable success in areas such as computer vision, speech recognition, natural language processing, and autonomous vehicles. Modern large language models, such as GPT, are built using deep learning techniques based on the Transformer architecture.
Natural Language Processing (NLP) focuses on enabling computers to understand, interpret, and generate human language. NLP applications include chatbots, language translation, sentiment analysis, text summarization, and question-answering systems. Recent advances in transformer-based models have significantly improved the quality of NLP applications.
As AI technology continues to evolve, ethical considerations have become increasingly important. Developers must ensure that AI systems are fair, transparent, secure, and respectful of user privacy. Responsible AI practices help minimize bias, improve accountability, and build trust among users while maximizing the positive impact of artificial intelligence on society."""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=0
)

#Perform the split
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)