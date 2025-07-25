def dotproduct(embedding1: list, embedding2: list):
    return sum(embedding1[i]*embedding2[i] for i in range(len(embedding1)))

def cosineSimilarity(embedding1: list, embedding2: list):
    dotproductValue = dotproduct(embedding1, embedding2)
    magnitude1 = dotproduct(embedding1,embedding1) ** 0.5
    magnitude2 = dotproduct(embedding2, embedding2) ** 0.5
    return dotproductValue/(magnitude1*magnitude2)

list1 = [1,2,3]
list2 = [1,2,3]
list3 = [-1,-2,-3]


##print(cosineSimilarity(list1,list2))
##print(cosineSimilarity(list1,list3))
