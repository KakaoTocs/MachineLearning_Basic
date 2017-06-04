# -*- coding: utf-8 -*- �ѱ��ּ� ���
import random

class ScrappyKNN():
	def fit(self, X_train, y_train):
		self.X_train = X_train
		self.y_train = y_train

	def predict(self, X_test):
		predictions = []
		for row in X_test:
			label = random.choice(self.y_train)
			predictions.append(label)
		return predictions


from sklearn import datasets
iris = datasets.load_iris()
#������ ��Ʈ�� �ҷ���

X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split
#�����ڵ�(from sklearn.cross_validation import train_test_split)�� ���� ����
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)
#Train, Test �����ͷ� ����

#from sklearn.neighbors import KNeighborsClassifier
my_classifier = ScrappyKNN()
#�ǻ����Ʈ���� ������ �ٸ� ������ �з���

my_classifier.fit(X_train, y_train)
#Train�����͸� �̿��� �з��� �Ʒ�

predictions = my_classifier.predict(X_test)
#��Ȯ�� �׽�Ʈ

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))