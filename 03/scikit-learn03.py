# -*- coding: utf-8 -*- 한글주석 사용
import numpy as np
import matplotlib.pyplot as plt

greyhounds = 500 
#그레이 하운드 500마리
labs = 500 
#래브라도 500마리

grey_height = 28 + 4 * np.random.randn(greyhounds) 
#그레이 하운드의 키 평균: 28인치, 4*난수를+
lab_height = 24 + 4 * np.random.randn(labs) 
#래브라도의 키 편균: 24인치,  4*난수를+

plt.hist([grey_height, lab_height], stacked=True, color=['r', 'b'])
#그레이 하운드는 빨간색으로 래브라도는 파랑색으로 표시
plt.show()