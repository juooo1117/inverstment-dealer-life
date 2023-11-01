# 2023 BIG CONTEST - KOSPI Stock Prediction
실제 주식(KOSPI) 데이터와 뉴스의 감성분석(Sentiment analysis)을 통한 '어린이 교육용 주식 예측 게임' 개발


## 🖥️ Project Introduction
### 어린이를 위한 주식교육 프로그램
   - 뉴스데이터와 KOSPI 정보를 분석 및 이용하여 구현된 뉴스기반 주식 등락 예측 교육용 프로그램
   - 게임 형식으로 어린이들에게 접근하는 교육 프로그램
   - 어린이들에게 흥미유발 및 지속적인 금융교육을 가능하게 하며, 자연스럽게 주식/경제 지식을 습득하여 금융능력을 함양할 수 있다.


 #### 1. 뉴스와 주가의 상관관계
   - 금융 시장은 정보의 흐름에 의존하므로 투자자들은 최신 경제, 금융, 정치 뉴스를 파악하여 투자를 결정함
   - 뉴스의 키워드와 내용은 투자 심리에 영향을 미치고 주가에 반영되므로, 주가 예측의 변수(variable)로 사용되기에 적합


 #### 2. 뉴스를 이용한 주가예측
   - 주식 시장은 정보의 흐름과 심리적 요소에 크게 영향을 받기 때문에 뉴스와 주가는 밀접한 관련성을 갖음
   - 각각의 뉴스마다 긍정(positive) or 부정(negative)적인 감성(sentiment)이 담겨있으므로, 텍스트를 분석하면 KOSPI stock 예측의 정보로 활용이 가능함   


 #### 3. 뉴스와 KOSPI 정보를 이용
   - 과거의 기업 KOSPI 등락의 흐름과 뉴스를 감성분석(Sentiment analysis)한 결과를 활용하여 주식 예측 모델에 반영하면 주식등라 예측 정확성을 높일 수 있음


## ✏️ Data Acquisition
### [주가데이터(KOSPI)]
#### (yahoo finance, https://finance.yahoo.com/)
   - 특정기간 동안의 기업별 KOSPI 정보를 수집하여, 수집된 정보 중 종가(Close) 데이터만 예측에 사용
   - 모델학습 및 데이터 분석에 활용한 기업과 각 기업별 KOSPI 수집기간은 아래와 같음

     |Enterprise(KS)|Collection Period|
     |------|------|
     |LG Chem, Ltd. (051910.KS)|2020/1/1 ~ 2022/12/31|
     |Hyundai Engineering & Construction Co., Ltd. (000720KS)|2018/1/1 ~ 2021/12/31|
     |Celltrion, Inc. (068270.KS)|2018/1/1 ~ 2021/12/31|
     |Samsung Biologics Co.,Ltd. (207940.KS)|2020/1/1 ~ 2022/12/31|
     |Ncsoft Corporation (036570.KS)|2018/1/1 ~ 2022/12/31|
     |SK hynix Inc. (000660.KS)|2020/1/1~ 2022/12/31|


### [뉴스데이터] 
#### (빅카인즈, https://www.bigkinds.or.kr/)
   - 통합데이터 빅카인즈 이용하여 기업별, 일자별로 기업 관련 뉴스 수집
   - 일자, 제목, 본문 내용 데이터를 예측에 사용

<p align="center">
  <img src="https://github.com/DagyeongH/inverstment-dealer-life/assets/95035134/bd66a2e4-afbe-4d21-bb9e-8a3fb581950f", width="750" height="400">
</p>


## 📖 Data Analysis & Pre-processing
 ### Okt(Open Korean Text)를 활용한 형태소 분석
   - 문장을 형태소 단위로 분해하고 각각의 형태소에 품사를 태깅
   - 중요한 정보를 담는 명사들만을 추출하여 사용한다


 ### Sentiment Analysis(감성분석)
   - 분해된 단어의 정보적 특징(feature)을 추출하여 text가 positive인지 negative인지를 분류한다.
   - 분석을 효과적으로 할 수 있도록 텍스트를 수치화하기 위함이 목적이다.
   - sentiment analysis를 뉴스 데이터의 수치화에 적용했으며, 주요 단계는 다음과 같이 진행된다.

   **[Sentiment Analysis Steps]**
      
      1) Text Data Collection
         - 특정 회사와 관련된 정보를 주가 예측 모델의 요소로 반영하고자 하므로, 수집할 데이터는 뉴스기사 형태의 텍스트 데이터이다.

      2) Text Pre-processing
         - 수집된 뉴스기사에서 불필요한 문자, 공백을 제거하고 tokenize하여 줄 글 형태의 텍스트를 단어나 구문으로 분할한다.
         - 이후에 형태소 분석을 통해 단어를 정규화(Normalization)하는 작업을 거친다.

      3) Feature Extraction
         - 텍스트 데이터를 수치화하기 위해서 Word-embedding 통해서 단어를 vector로 만들어준다.
         - 빈도적인 특징을 이용해서 TF-IDF로 가중치를 부여한다.

      4) Sentiment Classification
         - label이 지정되지 않은 새로운 텍스트를 training된 모델에 넣으면 해당 텍스트의 감정을 분류한다.
         - 긍정, 부정, 중립과 같은 label을 텍스트에 labeling 할 수 있다.


 ### TF-IDF(Term Frequency - Inverse Document Frequency)
   - 특정한 단어가 얼마나 자주 나타나는지, 그렇지 않은지를 측정하여 각각의 단어가 가진 중요도를 계산
   - 단어의 중요도가 계산되면 이 값은 각각의 단어에 반영된다.  


  ### Text Summarization
   - 문제에 사용될 뉴스 기사를 만들기 위해서 진행하며 추출적요약(extractive summarization)을 사용하여, 정보는 압축되지만 원본의 손실은 발생되지 않도록 하였다. 
   - 요약 후 문장의 개수를 지정할 수 있도록 하였고, 요약된 뉴스의 결과 예시는 아래와 같다. 즉, 사용자 대상 실제 문제는 아래의 내용으로 제공된다.

     |뉴스제목|요약된 내용|
     |------|--------|
     |"LG화학, 배터리 사업부 분사 수면 아래로... '실익 없다' 판단"|"LG화학이 전기자동차 배터리 사업을 분사하는 논의를 사실상 중단했다. 당분간 분사에 우호적인 환경이 조성되기 어렵다는게 대체적인 관측이다. LG화학은 지난해 하반기부터 사내 일각에서 검토하던 전지사업본부 분사 검토를 중단하고 당분간 현 체제를 유지하는 쪽으로 선회했다. 업계에서는 영업손실을 기록하고 있는 LG화학이 배터리 사업 분사를 중단한 결정을 '예견된 수순'으로 받아들이고 있다"|



## 🏆 Modeling

### LSTM(Long Short-Term Memory)
   시계열 예측(Timeseries forecasting)에 특화되어 있는 LSTM 모델을 미래 주가 등락 예측에 사용. LSTM은 순차 데이터에서 장거리 종속성을 유지할 수 있는 기능을 가지고 있어 이전의 데이터들을 이용하여 현재의 상태를 이해하고 예측하는 작업에 효과적이다. LSTM Architecture는 순환 신경망(RNN, Recurrent Neural Network)의 한 종류로 RNN Model의 한계인 Gradient Vanishing 문제를 극복한 구조이고, 시간적&순차적 특성을 가지고 있는 주식데이터의 특성을 고려하여 긴 시퀀스의 데이터를 효과적으로 학습할 수 있어서 LSTM Architecture를 modeling에 활용하였다.  


   **[LSTM Network]**
   <p align="center">
  <img src="https://github.com/DagyeongH/inverstment-dealer-life/assets/95035134/5beef3af-82f2-46a9-bddd-30b8a3fded7b", width="750" height="350">
</p>


### Model Training Sequence
#### 1.  단어(noun)별 'score' 계산
   - 각각의 단어가 존재하는 일자의 KOSPI 데이터를 가져온다.
   - 본 프로그램의 경우 미래의 주가 등락을 예측하는 것이기 때문에 각각의 단어가 가진 일자 다음 날의 KOSPI가 상승했으면 증가(1), 하락했으면 하락(0)을 tagging한다.
   - 단, 공휴일에 KOSPI는 데이터가 발생하지 않기 때문에, KOSPI가 없는 날짜에 발행된 뉴스에 해당하는 단어들은 구분하기 위하여 (-1)을 임의로 tagging 했다.


#### 2.  Vocab dictionary 생성 & score 반영
   - 추출된 단어 중에서 1글자인 명사는 삭제한 뒤, 2글자 이상으로 구성된 단어사전 'vocab'을 생성한다.
   - 'vocab'은 dictionary 형태로 만들어서 각 dictionary에 단어와 해당 단어의 점수(score)가 담겨있도록 구성한다.
   - 이 'vocab dictionary'는 KOSPI 등락에 따른 변화 정보를 반영하고 있으며, 형태는 아래의 표와 같다.

     |단어(noun)|Vocab dictionary(dict 형태)|
     |---------|--------------------------|
     |1|{'스타트업': -11.965999999999987}|
     |2|{'인테리어': 0.01200000000000001}|
     |3|{'어디': -0.2779999999999996}|
     |4|{'소비자': -0.43399999999999994}|


#### 3.  TF-IDF 적용
   - 'vocab' 안에 담긴, 계산된 score를 가진 'noun'을 일자별로 묶어준다.
   - 개별적인 단어가 가진 score를 보다 정확히 하기 위해서 이렇게 묶인 단어들에 다시 KOSPI 등락에 따른 상승(1), 하락(0) 값을 tagging한 뒤에 각 일자 별로 묶여있는 단어들의 TF와 IDF를 구한다.
   - 각각 구한 TF, IDF 값으로 'vocab'에 들어있는 단어 별 TF-IDF 값을 구하고, 'vocab'안의 각각의 단어 별로 원래 할당되어있던 값을 곱해서 최종적인 단어별 score를 구한다.
   - 각 단어들은 최종적으로 아래와 같은 score를 갖는다.

<p align="center">
  <img src="https://github.com/DagyeongH/inverstment-dealer-life/assets/95035134/4af81ab3-fec5-4794-ba11-5b5daee92f22", width="750" height="400">
</p>


#### 4.  LSTM Model 적용
   - 'keras'의 LSTM 모델 패키지를 불러와 학습에 활용 ('Sequential' 모델 활용)
   - 학습이 잘 되었는지 확인하기 위해서 train data[80%], test data[20%]로 나누어서 학습을 진행
   - 회사별로 KOSPI와 관련된 뉴스가 다르므로, 회사별로 나누어서 개별적으로 training을 진행했다.
   - 각 회사마다 batch size와 epoch은 조절하면서 model을 train했고, 출력된 정확도(accuracy)는 아래의 표와 같다.

     |Enterprise(KS)|Accuracy|val_accuracy|Epoch|
     |--------------|--------|------------|-----|
     |LG Chem, Ltd. (051910.KS)|0.6708|0.7042|20|
     |Hyundai Engineering & Construction Co., Ltd. (000720KS)|0.648|0.5677|30|
     |Celltrion, Inc. (068270.KS)|0.6561|0.6474|30|
     |Samsung Biologics Co.,Ltd. (207940.KS)|0.7074|0.6879|30|
     |Ncsoft Corporation (036570.KS)|0.6284|0.6376|30|
     |SK hynix Inc. (000660.KS)|0.712|0.7194|30|


#### 5.  Test-data generate
   - 빅카인즈에서 가져온 뉴스 데이터를 일부를 사용하여 뉴스 본문을 요약하는 작업 진행
   - 뉴스내용을 요약하기 위해 필요한 라이브러리인 'feedparser', 'newspaper3k', 'summa'를 사용
   - 만들어진 뉴스 본문 요약 내용은 차후 user에게 보여주는 과정에서 사용
 

### [Result] 주가 등락 결과 예측
   - 뉴스를 요약해서 생성한 test-data로 단어의 'score'를 구해서 모델의 input으로 넣고, 주가의 상승(1) 또는 하락(0) 여부를 예측한다.
   - 한 개의 input에 대한 예측결과의 예시는 <array([[1.28374006e-17]], dtype=float32)> 로, 0에 가까운 값이 나왔기 때문에 모델 예측 결과값은 '하락'이다.
   - 모델 예측 결과는 실제로 문제에 활용하기 위해서 json형식으로 변환하여 사용한다.


## 🖥️ Programme
분석결과를 이용해서 django로 실제로 어린이들을 위한 주식 교육용 게임 프로그램을 구현하였다.


### Logic & User 화면
   - 메인: 랜덤으로 문제 중 10개를 선택
   - 뉴스피드: 랜덤문제 10개 중 임의로 3개만 선택해서 출력
   - 퀴즈: 뉴스기사를 읽고 주가 하락 or 상승을 예측
   - 힌트: 힌트버튼을 누르면 어려운 경제용어의 뜻풀이가 출력
   - 퀴즈결과: 사용자가 맞춘 답을 점수로 변환하여 출력
   - 오답노트: 틀린 문제는 한 번 더 확인할 수 있도록 제공


   **[User 화면]**
<p align="center">
  <img src="https://github.com/DagyeongH/inverstment-dealer-life/assets/95035134/ae518300-42ee-4ba2-a187-69489865d1c5">
</p>

<p align="center">
  <img src="https://github.com/DagyeongH/inverstment-dealer-life/assets/95035134/361ad2d3-bdd2-4145-8127-4d343868abba">
</p>



## 🕰️ 개발 기간
- 2023.08.31 ~ 2023.09.27

## 👩🏻‍💻 팀원
- 박주현
- 홍다경
- 박채원
- 김지인

## 🛠 개발환경
- Django
- konlpy
- MECAB

## 📚 데이터
- 데이터는 [여기서](https://drive.google.com/drive/folders/1arbxmEQmTBWxk4C6Jb6BagznDC0onNT9?usp=sharing) 다운로드 가능 ! 
  

