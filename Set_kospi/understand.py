"""
News_sentiment_analysis_3.ipynb 파일 기준 이해를 위한 파일
"""

from sklearn.model_selection import train_test_split

df_train, df_test = train_test_split(df, test_size=0.3, random_state=777)
"""
train_test_split 함수는 scikit-learn 라이브러리에서 제공하는 함수로, 데이터를 훈련 세트(train set)와 테스트 세트(test set)로 나누는 데 사용됩니다. 이것은 기계 학습 모델을 훈련하고 모델의 성능을 평가하는 데 유용합니다. 
> df라는 데이터프레임을 70%의 훈련 세트(df_train)와 30%의 테스트 세트(df_test)로 나누고 있습니다.
"""


df_train = df_train[['일자', '제목', 'updown', 'nouns']]
"""
'일자': 날짜 정보가 있는 열.
'제목': 텍스트 제목 정보가 있는 열.
'updown': 주식 등락 정보가 있는 열. ('증가': 1, '감소': 0, 그 외: -1)
'nouns': 명사 정보가 있는 열.
"""

#2차 불용어 제거
df_train['제목'] = df_train['제목'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","", regex=True)
df_train['제목'].replace('', np.nan, inplace=True)
df_train = df_train.dropna(how='any')
"""
'제목' 열에서 한글 이외의 문자를 제거하고, 빈 문자열로 대체한 뒤, 빈 문자열을 가진 행을 제거.

df_train['제목'] = df_train['제목'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","", regex=True): '제목' 열에서 한글 이외의 문자(특수 문자, 숫자 등)를 정규 표현식을 사용하여 제거합니다. [^ㄱ-ㅎㅏ-ㅣ가-힣 ]는 한글 및 공백을 제외한 모든 문자를 나타내는 정규 표현식입니다. 따라서 한글과 공백 이외의 모든 문자가 삭제됩니다.

df_train['제목'].replace('', np.nan, inplace=True): 빈 문자열을 NaN(결측치)으로 대체합니다. 이 단계를 통해 빈 문자열을 NaN 값으로 표시하고 나중에 이를 처리할 수 있습니다.

df_train = df_train.dropna(how='any'): NaN 값을 가진 행을 제거합니다. 'how' 매개변수를 'any'로 설정하면 하나라도 NaN 값을 포함하는 행을 제거합니다. 이렇게 하면 빈 문자열을 가진 행이 제거되고, 정제된 데이터가 남습니다.

결과적으로 '제목' 열에서 한글 이외의 문자를 제거하고 빈 문자열을 가진 행을 제거한 데이터프레임이 생성됩니다. 이렇게 전처리된 데이터를 활용하여 텍스트 분석이나 기계 학습 모델을 훈련하는 데 사용할 수 있습니다.
"""


vocab = {}
cnt = 0
for i in df_train['nouns']:
  i = i.split(' ')
  for j in range(len(i)):
    if i[j] in vocab or len(i[j]) <= 1:
      cnt += 1
      pass
    else:
      vocab[i[j]] = 0
vocab

"""
vocab = {}: 빈 딕셔너리인 vocab을 초기화합니다. 이 딕셔너리는 단어장을 저장하는데 사용됩니다.

cnt = 0: 빈도가 1 미만인 단어나 이미 vocab에 있는 단어의 수를 저장할 변수 cnt를 초기화합니다.

for i in df_train['nouns']:: 'nouns' 열에서 각 행의 명사를 가져오는 반복문을 시작합니다.

i = i.split(' '): 각 행의 명사를 공백을 기준으로 분리하여 리스트로 만듭니다.

for j in range(len(i)):: 분리된 명사 리스트를 순회하면서 각 명사를 처리합니다.

if i[j] in vocab or len(i[j]) <= 1:: 현재 명사가 이미 vocab 딕셔너리에 있거나 길이가 1 이하인 경우, cnt를 증가시키고 넘어갑니다. 이렇게 하면 단어장에 추가되지 않습니다.

else: 그렇지 않은 경우(길이가 2 이상이고 처음 등장하는 명사), vocab 딕셔너리에 해당 단어를 추가하고 초기 빈도를 0으로 설정합니다.

이 코드를 실행하면 'nouns' 열에서 추출한 명사들을 단어장으로 정리하고, 각 단어의 빈도를 초기화한 결과가 vocab 딕셔너리에 저장됩니다. 이렇게 생성된 단어장은 후속 분석이나 기계 학습 모델 학습에 사용될 수 있습니다.

"""
"""
7817 {'삼성': 0, '테일러': 0, '파운드리': 0, '공장': 0, '고객': 0,  ...}
"""

up = 4928
down = 4471
up_ratio = up/(up+down)
down_ratio = down/(up+down)

import collections
for i,w in enumerate(df_train['nouns']):
    w = w.split(' ')
    if (df_train.iloc[i]['updown']==1):
        for j in range(len(w)):
            noun = w[j]
            if len(noun)<=1:
              continue
            vocab[noun] = vocab[noun] + down_ratio
    else:
        for j in range(len(w)):
            noun = w[j]
            if len(noun)<=1:
              continue
            vocab[noun] = vocab[noun] - up_ratio
"""
up 및 down: 'up'은 상승한 날짜의 수, 'down'은 하락한 날짜의 수를 나타냅니다. 이를 이용하여 상승 및 하락 비율(up_ratio 및 down_ratio)을 계산합니다.

collections.Counter()를 사용하여 단어 빈도를 추적하는 딕셔너리인 vocab을 생성합니다. 이 딕셔너리는 단어와 그에 대한 가중치를 저장하는 데 사용됩니다.

vocab[noun] = vocab[noun] + down_ratio: 상승한 날짜의 경우, 해당 명사의 가중치에 down_ratio를 더합니다.

위와 유사한 과정을 하락한 날짜에 대해서 수행하며, 가중치에 - up_ratio를 더합니다.

이렇게 하면 명사 단어의 등락에 따라 가중치가 조절되며, 텍스트 데이터를 반영하여 모델 학습에 활용될 수 있습니다.
"""


total = []
sent_dictionary = vocab
for i,w  in enumerate(new_df_train['nouns']):
    sent_score = 0
    w= w.split(' ')
    for j in w:
        if(len(j)<=1):
          continue
        elif(j not in sent_dictionary):
          continue
        else:
          sent_score = sent_score + sent_dictionary[j]
    total.append(sent_score/len(w))
new_df_train['sent_score'] = total
"""
주어진 코드는 new_df_train 데이터프레임에서 'nouns' 열의 각 행을 처리하여 단어의 가중치를 합산하고, 이를 평균화한 sent_score 열을 생성하는 작업을 수행합니다. 이렇게 생성된 sent_score는 각 날짜의 텍스트 데이터에 대한 감성 점수를 나타냅니다.

total = []: 각 날짜의 텍스트 데이터에 대한 감성 점수를 저장할 빈 리스트인 total을 초기화합니다.

sent_dictionary = vocab: vocab 딕셔너리를 sent_dictionary에 할당합니다. 이 딕셔너리는 단어와 그에 대한 가중치를 포함합니다.

sent_score = 0: 현재 날짜의 감성 점수를 초기화합니다.

else: 그렇지 않은 경우, 명사의 가중치를 sent_score에 더합니다.

total.append(sent_score / len(w)): 현재 날짜의 감성 점수를 해당 날짜의 명사 개수로 나누어 평균화한 후, total 리스트에 추가합니다.

new_df_train['sent_score'] = total: 감성 점수가 계산된 total 리스트를 'sent_score' 열로 추가합니다.

이렇게 하면 각 날짜에 대한 텍스트 데이터의 감성 점수가 계산되어 'sent_score' 열에 저장됩니다. 이 점수는 해당 날짜의 텍스트 데이터에 대한 감정 또는 가중치 정보를 나타냅니다.
"""


##모델링

new_df_train.dropna(inplace=True)
"""
new_df_train.dropna(inplace=True) 코드는 new_df_train 데이터프레임에서 NaN 값을 가진 행을 제거하는 작업을 수행합니다.
"""


ndt_drop['sent_score'] = ndt_drop['sent_score'] / 100

train_data, validation_data = train_test_split(ndt_drop, test_size = 0.2, random_state = 42)
mecab = Mecab()
trainX = train_data['sent_score'].values
trainY = train_data['updown'].values
testX = validation_data['sent_score'].values
testY = validation_data['updown'].values
"""
주어진 코드는 데이터의 전처리 및 학습 데이터와 검증 데이터로 분할하는 작업을 수행합니다. 이 작업은 주로 텍스트 데이터를 감성 분석 모델을 훈련하고 평가하기 위한 준비과정입니다.

ndt_drop['sent_score'] = ndt_drop['sent_score'] / 100: 'sent_score' 열의 값을 100으로 나누어 스케일링하는 작업을 수행합니다. 이 작업은 데이터를 정규화하거나 스케일링하여 모델 학습에 도움을 주는 일반적인 전처리 방법 중 하나입니다.

train_test_split: 데이터를 학습 데이터와 검증 데이터로 나누는 작업을 수행합니다. test_size 매개변수를 사용하여 검증 데이터의 비율을 설정할 수 있습니다.

mecab = Mecab(): 한국어 형태소 분석기인 Mecab을 초기화합니다. 이는 한국어 텍스트 데이터를 토큰화하고 형태소로 분리하는 데 사용됩니다.

trainX, trainY, testX, testY: 학습 데이터와 검증 데이터를 준비합니다. trainX는 학습 데이터의 'sent_score' 열의 값을, trainY는 'updown' 열의 값을 각각 포함하고, testX와 testY는 검증 데이터의 값을 포함합니다.

이렇게 전처리된 데이터는 딥러닝 모델을 훈련하고 검증하기 위해 사용될 수 있습니다. trainX와 trainY는 모델의 입력과 출력을 나타내며, testX와 testY는 모델의 성능을 평가하는 데 사용됩니다.

"""


model = Sequential()

model.add(Dense(32, activation='relu', input_shape=(1,)))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer=tf.keras.optimizers.RMSprop(lr=0.0001),   # learning rate 조정
              loss='binary_crossentropy',
              metrics=['accuracy'])

es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=4)

model.fit(trainX, trainY,
          validation_data=(testX, testY),
          callbacks=es,
          batch_size=32,
          epochs=30)
"""
주어진 코드는 Keras를 사용하여 간단한 이진 분류 모델을 생성하고 훈련하는 과정을 나타냅니다. 이 모델은 'sent_score'를 입력으로 받아 'updown'을 예측하는 이진 분류 작업을 수행합니다. 간단한 모델의 구성과 훈련 과정은 다음과 같습니다:

1. `model = Sequential()`: Sequential 모델을 생성합니다. Sequential 모델은 층(layer)을 순차적으로 쌓아가는 방식의 신경망 모델입니다.

2. `model.add(Dense(32, activation='relu', input_shape=(1,)))`: 모델에 첫 번째 밀집(Dense) 층을 추가합니다. 이 층은 32개의 뉴런을 가지며 활성화 함수로 ReLU를 사용합니다. 입력의 크기는 (1,)로 설정되어 'sent_score' 열의 값을 입력으로 받습니다.

3. `model.add(Dense(1, activation='sigmoid'))`: 두 번째 밀집 층을 추가합니다. 이 층은 1개의 뉴런을 가지며 활성화 함수로 시그모이드 함수를 사용합니다. 이 층은 이진 분류 문제를 다루기 위해 사용됩니다.

4. `model.compile(...)`: 모델을 컴파일합니다. 옵티마이저로는 RMSprop를 사용하며, 학습률(learning rate)은 0.0001로 설정됩니다. 손실 함수로는 이진 분류 문제에 적합한 'binary_crossentropy'를 사용하고, 정확도(accuracy)를 모델의 성능 지표로 설정합니다.

5. `es = EarlyStopping(...)`: 조기 종료(Early Stopping) 콜백을 설정합니다. 검증 손실(validation loss)을 모니터링하며, 손실이 4번 연속으로 개선되지 않으면 훈련을 조기 종료합니다.

6. `model.fit(...)`: 모델을 훈련합니다. 학습 데이터인 `trainX`와 `trainY`를 사용하여 모델을 학습하고, 검증 데이터인 `testX`와 `testY`를 사용하여 모델의 성능을 평가합니다. 콜백으로 조기 종료 콜백 `es`를 사용하며, 배치 크기는 32로 설정하고 총 30 에포크 동안 훈련을 수행합니다.

이렇게 구성된 모델은 학습 데이터로부터 'sent_score'를 입력으로 받아 'updown'을 예측하는 모델로, 이진 분류 작업에 적합합니다. Early Stopping을 통해 과적합을 방지하면서 모델의 성능을 향상시킬 수 있습니다.
"""