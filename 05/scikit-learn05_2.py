# -*- coding: utf-8 -*- �ѱ��ּ� ���
from scipy.spatial import distance

def euc(a, b):
	return distance.euclidean(a, b)
	#������ �Ÿ� ��

class ScrappyKNN():
	def fit(self, X_train, y_train):
		self.X_train = X_train
		self.y_train = y_train
		#train������ ����

	def predict(self, X_test):
		predictions = []
		for row in X_test:
			label = self.closest(row)
			predictions.append(label)
		return predictions

	def closest(self, row):
		best_dist = euc(row, self.X_train[0])
		best_index = 0
		for i in range(1, len(self.X_train)):
			dist = euc(row, self.X_train[i])
			if dist < best_dist:
				best_dist = dist
				best_index = i
		return self.y_train[best_index]


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