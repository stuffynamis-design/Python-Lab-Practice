import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
data=pd.read_csv(r"C:\\Users\\GAMER\\Downloads\\iris(4).csv")
print("first five rows of the dataset")
X=data[["sepal_length","sepal_width","petal_lenth","petal_width"]]
y=data[["species"]]
X_train,X_test,y_train,y_test=train_test_split(test_size =0.5,random_states=42)
model=KNeighborsClassifier(n_neighbors=3)
model_fit=(X_train,y_train)
y_pred=model.prdict(X_test)
accuracy=accuracy_score(y_test,y_pred)
print("Accuracy:",accuracy*100,"%")
