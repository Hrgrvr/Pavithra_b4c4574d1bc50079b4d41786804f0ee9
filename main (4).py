'''
Write a function called linear_search_product that takes the list of products and a target product
name as input. The function should perform a linear search to find the target product in the list and 
return a list of indices of all occurrences of the product if found, or an empty list if the product is not
found.'''

def linearSearchProduct(productList,  targetProduct):
  indices=[]

  for index, product in enumerate(productList):
    if product==targetProduct:
      indices.append(index)

  return indices



Product=["Shoes","boot","Loafer","Shoes","Sandal","Shoes"]
target="Shoes"
target2="apple"
result=linearSearchProduct(Product,target)
print(result)