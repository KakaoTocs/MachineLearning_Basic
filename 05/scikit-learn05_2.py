# -*- coding: utf-8 -*- 한글주석 사용
from scipy.spatial import distance

def euc(a, b):
	return distance.euclidean(a, b)
	#두점의 거리 비교

class ScrappyKNN():
	def fit(self, X_train, y_train):
		self.X_train = X_train
		self.y_train = y_train
		#train데이터 저장

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
#데이터 세트를 불러옴

X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split
#기존코드(from sklearn.cross_validation import train_test_split)는 경고로 변경
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)
#Train, Test 데이터로 나눔

#from sklearn.neighbors import KNeighborsClassifier
my_classifier = ScrappyKNN()
#의사결정트리를 대차한 다른 종류의 분류자

my_classifier.fit(X_train, y_train)
#Train데이터를 이용해 분류자 훈련

predictions = my_classifier.predict(X_test)
#정확도 테스트

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))