# -*-coding:utf-8-*-
from sklearn import tree
features = [[140,1], [130, 1], [150,0], [170, 0]]
#[무개, 0:거친것 or 1:부드러운것]
labels = [0, 0, 1, 1]
#0:사과 or 1:오랜지

clf = tree.DecisionTreeClassifier()
#분류자 생성(현재는 비어 있는 구칙 박스)
clf = clf.fit(features, labels)
#분류자에 룰 생성(fit의 뜻은 규칙을 발견 했다.)

print(clf.predict([[150, 0]]))
#크기가 150에 거친것은 오렌지(거친것은 오렌지뿐)