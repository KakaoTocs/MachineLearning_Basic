# -*-coding:utf-8-*-
from sklearn import tree
features = [[140,1], [130, 1], [150,0], [170, 0]]
#[����, 0:��ģ�� or 1:�ε巯���]
labels = [0, 0, 1, 1]
#0:��� or 1:������

clf = tree.DecisionTreeClassifier()
#�з��� ����(����� ��� �ִ� ��Ģ �ڽ�)
clf = clf.fit(features, labels)
#�з��ڿ� �� ����(fit�� ���� ��Ģ�� �߰� �ߴ�.)

print(clf.predict([[150, 0]]))
#ũ�Ⱑ 150�� ��ģ���� ������(��ģ���� ��������)