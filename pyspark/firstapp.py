from pyspark import SparkContext

# 计算 README.md 文件中带有字符“a”的行数
logFile = "./readme.md"  
sc = SparkContext("local", "first app")
logData = sc.textFile(logFile).cache()
numAs = logData.filter(lambda s: 'a' in s).count()
print("Lines with a: %i" % (numAs))

print(logData.persist().is_cached)
print(logData.getStorageLevel())