# -*-coding:utf-8-*-
from sklearn import tree
import pydotplus
features = [[140,1], [130, 1], [150,0], [170, 0]]
#[����, 0:��ģ�� or 1:�ε巯���]
labels = [0, 0, 1, 1]
#0:��� or 1:������

part = ["Weigh", "textur"]
name = ["Apple", "Orange"]

clf = tree.DecisionTreeClassifier()
#�з��� ����(����� ��� �ִ� ��Ģ �ڽ�)
clf = clf.fit(features, labels)
#�з��ڿ� �� ����(fit�� ���� ��Ģ�� �߰� �ߴ�.)

print(clf.predict([[150, 0]]))
print(clf.predict([[170, 1]]))
#ũ�Ⱑ 150�� ��ģ���� ������(��ģ���� ��������)
#�� ������ ���Է� ������ ���
'''
from sklearn.externals.six import StringIO
import pydot
dot_data = StringIO()
tree.export_graphviz(clf,
			out_file=dot_data,
			feature_names=part,
			class_names=name,
			filled=True, rounded=True,
			impurity=False)

graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("tree1.pdf")
'''