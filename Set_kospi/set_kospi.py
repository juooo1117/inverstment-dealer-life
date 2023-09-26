import pandas as pd
import re
import os
import numpy as np

"""
코드를 더 간단하게 업데이트 해봤는데 크게 달라진점이 있다면
원래 등락의 비율을 
그 날의 '코스피 평균값'을 구해서 전날이랑 비교를 했다면,
종가만 가지고 전날이랑 비교해서 등락비율을 구해놓음.   
"""

# 현재 폴더 확인 및 지정
currentPath = os.getcwd()

kospis_data = pd.read_csv(currentPath + '/kospi.csv')
# print(kospis_data)

# 날짜를 datetime 형식으로 변환
kospis_data['Date'] = pd.to_datetime(kospis_data['Date'])


# 날짜와 종가만 사용
kospi_day = kospis_data[['Date', 'Close']].copy()
# print(kospi_day[:5])
"""
        Date        Close
0 2022-09-05  2403.679932
1 2022-09-06  2410.020020
2 2022-09-07  2376.459961
3 2022-09-08  2384.280029
4 2022-09-13  2449.540039
"""

# 등락 비율 계산
# pct_change() : pandas의 내장 함수 시리즈(열) 내의 각 값에서 이전 값과의 백분율 변화를 계산. 각 행에서의 일일 등락율을 얻을 수 있음.
# fillna(0): NaN(결측치) 값을 0으로 대체합니다
kospi_day['Return'] = kospi_day['Close'].pct_change().fillna(0)
# print(kospi_day[:5])
"""
        Date        Close    Return
0 2022-09-05  2403.679932  0.000000
1 2022-09-06  2410.020020  0.002638
2 2022-09-07  2376.459961 -0.013925
3 2022-09-08  2384.280029  0.003291
4 2022-09-13  2449.540039  0.027371
"""

# 등락 결과 계산
"""
np.where(condition, x, y) : 조건만족의 경우 x, 아니면 y를 반환
kospi_day['Return'] > 0 : 양수
kospi_day['Return'] < 0 : 음수
'변동없음' : 두개의 조건이 모두 아닐 경우 else와 같음. 
"""
kospi_day['Result'] = np.where(kospi_day['Return'] > 0, '증가', np.where(kospi_day['Return'] < 0, '감소', '변동없음'))

# 감소한 날짜와 증가한 날짜 분류
kospi_up_date = kospi_day[kospi_day['Result'] == '증가']['Date']
kospi_down_date = kospi_day[kospi_day['Result'] == '감소']['Date']

# print("감소한 날짜:", kospi_down_date.tolist()[:5])
# print("증가한 날짜:", kospi_up_date.tolist()[:5])
"""
감소한 날짜: [Timestamp('2022-09-07 00:00:00'), Timestamp('2022-09-14 00:00:00'), Timestamp('2022-09-15 00:00:00'), Timestamp('2022-09-16 00:00:00'), Timestamp('2022-09-19 00:00:00')]
증가한 날짜: [Timestamp('2022-09-06 00:00:00'), Timestamp('2022-09-08 00:00:00'), Timestamp('2022-09-13 00:00:00'), Timestamp('2022-09-20 00:00:00'), Timestamp('2022-09-27 00:00:00')]
"""


