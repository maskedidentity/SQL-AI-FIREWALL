from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib import request, error
import pandas as pd
import numpy as np
from pycaret.clustering import *
import urllib.parse
import sys

badwords = ['sleep','SLEEP','update','UPDATE','drop','DROP','uid','UID','select','SELECT','waitfor','WAITFOR','delay','DELAY','system','SYSTEM','union','UNION','order by','ORDER BY','group by','GROUP BY','and','AND','insert','INSERT','delete','DELETE','create','CREATE','alter','ALTER','truncate','TRUNCATE','or','OR','cast','CAST','exec','EXEC','execute','EXECUTE','declare','DECLARE','table','TABLE','schema','SCHEMA','varchar','VARCHAR','char','CHAR','nvarchar','NVARCHAR','int','INT','bool','BOOL','boolean','BOOLEAN','where','WHERE','having','HAVING','case','CASE','when','WHEN','then','THEN','else','ELSE','drop table','DROP TABLE','information_schema','INFORMATION_SCHEMA','from','FROM','insert into','INSERT INTO','update set','UPDATE SET','set','SET','values','VALUES','order','ORDER','join','JOIN','left join','LEFT JOIN','inner join','INNER JOIN','right join','RIGHT JOIN','outer join','OUTER JOIN','all','ALL']
def ExtractFeatures(path):
    path = urllib.parse.unquote(path)
    badwords_count = 0
    single_q = path.count("'")
    double_q = path.count("\"")
    dashes = path.count("--")
    braces = path.count("(") 
    spaces = path.count(" ") 
    for word in badwords:
        badwords_count += path.count(word)
    lst= [single_q, double_q, dashes, braces, spaces, badwords_count]
    print(lst)
    return pd.DataFrame([lst], columns = ['single_q','double_q','dashes','braces','spaces','badwords'])

http = pd.read_csv(r'C:\Users\LENOVO\exp\exp\all.csv')

# Initialize PyCaret setup for clustering
clu1 = setup(data=http, 
             numeric_features = ['single_q', 'double_q', 'dashes', 'braces', 'spaces', 'badwords'],
             ignore_features = ['method', 'path', 'body', 'class'])


http = http.dropna(subset = ['single_q', 'double_q', 'dashes', 'braces', 'spaces', 'badwords'])

#print(http[['single_q', 'double_q', 'dashes', 'braces', 'spaces', 'badwords']].isnull().sum())
#print(http[['single_q', 'double_q', 'dashes', 'braces', 'spaces', 'badwords']].applymap(lambda x: not np.isfinite(x)).sum())


# Create KMeans model with 2 clusters
kmeans = create_model('kmeans', num_clusters=2)

result = predict_model(kmeans, data=http)
# View the data with assigned clusters
print(result[['single_q', 'double_q', 'dashes', 'braces', 'spaces', 'badwords', 'Cluster']])

    
    
