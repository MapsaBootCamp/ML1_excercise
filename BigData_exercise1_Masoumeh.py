import pyspark
import findspark
#findspark.init()
#findspark.init("/home/mvali/Desktop/Jupyter_Project/")
from pyspark.sql import SparkSession

from pyspark.sql import SparkSession
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
from pandas.plotting import scatter_matrix

spark = SparkSession.builder.appName("Divar").getOrCreate()

spark
#Load & Analysis Data
df=spark.read.csv('DivarFinal.csv',inferSchema=True,header=True)
df.printSchema()
print('Columns overview')
pd.DataFrame(df.dtypes, columns = ['Column Name','Data type'])
df.show()
df.summary().show()
df.describe().toPandas()
pd.DataFrame(df.take(10), columns=df.columns).transpose()
df.count()
for col in df.columns:
    print(col, "with null values: ", df.filter(df[col].isNull()).count())

 #House with less than 5 years of construction.   
print("Number of houses with less than 5 years of construction:",df.filter(df['Year'] > 1396).count())
#groupby Price per meter 
gp = df.groupBy("Price per meter").count()
gp.show(10)
numeric_features = [t[0] for t in df.dtypes if t[1] == 'int']
numeric_data = df.select(numeric_features).toPandas()
axs = scatter_matrix(numeric_data, figsize=(20, 20))
n = len(numeric_data.columns)

for i in range(n):
    v = axs[i, 0]
    v.yaxis.label.set_rotation(0)
    v.yaxis.label.set_ha('right')
    v.set_yticks(())
    h = axs[n-1, i]
    h.xaxis.label.set_rotation(90)
    h.set_xticks(())

#Correlation between variables and Price
import six
for i in df.columns:
    if not( isinstance(df.select(i).take(1)[0][0], six.string_types)):
        print( "Correlation to Price for ", i, df.stat.corr('Price',i))

#Linear Regression model 
from pyspark.ml.feature import VectorAssembler
vectorAssembler = VectorAssembler(inputCols = ["Area", "Year", "Number Of Room", "Price per meter", "Floor", "Elevator"\
                                              , "Parking", "Warehouse"], outputCol = 'features')
vector_df = vectorAssembler.transform(df)
vector_df = vector_df.select(['features', 'Price'])
vector_df.show(3)

splits = vector_df.randomSplit([0.7, 0.3])
train_df = splits[0]
test_df = splits[1]

from pyspark.ml.regression import LinearRegression
lr = LinearRegression(featuresCol = 'features', labelCol='Price', maxIter=10, regParam=0.3, elasticNetParam=0.8)
lr_model = lr.fit(train_df)
print("Coefficients: " + str(lr_model.coefficients))
print("Intercept: " + str(lr_model.intercept))

trainingSummary = lr_model.summary
print("RMSE: %f" % trainingSummary.rootMeanSquaredError)
print("r2: %f" % trainingSummary.r2)


train_df.describe().show()


lr_predictions = lr_model.transform(test_df)
lr_predictions.select("prediction","Price","features").show(5)
from pyspark.ml.evaluation import RegressionEvaluator
lr_evaluator = RegressionEvaluator(predictionCol="prediction", \
                 labelCol="Price",metricName="r2")
print("R Squared (R2) on test data = %g" % lr_evaluator.evaluate(lr_predictions))

test_result = lr_model.evaluate(test_df)
print("Root Mean Squared Error (RMSE) on test data = %g" % test_result.rootMeanSquaredError)

predictions = lr_model.transform(test_df)
predictions.select("prediction","Price","features").show()




