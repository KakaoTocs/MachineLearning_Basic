# -*- coding: utf-8 -*- 한글주석 사용
from sklearn import datasets
iris = datasets.load_iris()
#데이터 세트를 불러옴

X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split
#기존코드(from sklearn.cross_validation import train_test_split)는 경고로 변경
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)
#Train, Test 데이터로 나눔

'''
from sklearn import tree
my_classifier = tree.DecisionTreeClassifier()
'''
from sklearn.neighbors import KNeighborsClassifier
my_classifier = KNeighborsClassifier()
#의사결정트리를 대체한 다른 종류의 분류자

my_classifier.fit(X_train, y_train)
#Train데이터를 이용해 분류자 훈련

predictions = my_classifier.predict(X_test)
#정확도 테스트
#print(predictions)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))