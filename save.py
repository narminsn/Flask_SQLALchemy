from  models import *

url=["https://cdn-images-1.medium.com/max/1600/1*olJUeL2ziDvUPnXBBbPCYA.jpeg","https://www.mondo.com/wp-content/uploads/2018/02/in-demand-programming-languages.jpg",]
name=["PostgreSql","Sql Server"]

for i in range(len(url)):
    a=Portfolio(image=url[i],project_name=name[i])
    a.save()

print("OK")