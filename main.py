from CosineSimilarity import CosineSimilarity

if __name__ == '__main__':
    # query = input("Enter your query: ")
    query = "online retail markets"
    cs = CosineSimilarity(query)
    print("QUERY 1 : ", query)
    print(cs.get_similar_documents())
    print()

    query = "profitable venture of computer"
    cs = CosineSimilarity(query)
    print("QUERY 2 : ", query)
    print(cs.get_similar_documents())
    print()

    query = "messaging app available on android"
    cs = CosineSimilarity(query)
    print("QUERY 3 : ", query)
    print(cs.get_similar_documents())
    print()