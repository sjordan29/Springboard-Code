import findspark 
findspark.init()
import pyspark 
sc = pyspark.SparkContext()


list1 = sc.parallelize(range(1,1000)).map(lambda x: x*10)

# reduce function
num = list1.reduce(lambda x,y: x+y)

#filter 
# collect is a list/rdd method 
list2 = list1.filter(lambda x: x%100 == 0).collect()

# take first 5 
list3 = list1.filter(lambda x: x%100 == 0).take(5)

# transformations return another RDD
# lazy - don't actually do anything
# map, filter, flatmap

# actions return a value other than an RDD
# performed immediately 
# reduce, take, collect, sum, max, min, mean 


# Get an RDD with number 1 to 10 

rdd = sc.parallelize(range(1,10))

# Get the elements in that RDD which are divisible by 3

div3 = rdd.filter(lambda x: x%3 ==0)
div_3 = div3.collect()
print(div_3)

# Get the product of the elements in ^
product = div3.reduce(lambda x,y: x*y)
print(product)

# To read a text file
# people = sc.textFile(urlOrPath, minPartitions, useUnicode=True)
# gives an rdd of strings (one per line)
# e.g. people = sc.textFile("data/people.txt")
# to split a tab delimited file: people.map(lambda x: x.split('\t'))


