# -*- coding: utf-8 -*- �ѱ��ּ� ���
import numpy as np
import matplotlib.pyplot as plt

greyhounds = 500 
#�׷��� �Ͽ�� 500����
labs = 500 
#����� 500����

grey_height = 28 + 4 * np.random.randn(greyhounds) 
#�׷��� �Ͽ���� Ű ���: 28��ġ, 4*������+
lab_height = 24 + 4 * np.random.randn(labs) 
#������� Ű ���: 24��ġ,  4*������+

plt.hist([grey_height, lab_height], stacked=True, color=['r', 'b'])
#�׷��� �Ͽ��� ���������� ����󵵴� �Ķ������� ǥ��
plt.show()