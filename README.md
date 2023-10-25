# 2023 BIG CONTEST - KOSPI Stock Prediction
실제 주식(KOSPI) 데이터와 뉴스의 감성분석(Sentiment analysis)을 통한 '어린이 교육용 주식 예측 게임' 개발


## 🖥️ Project Introduction
  어린이를 위한 주식교육 프로그램
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


## ✏️ Data Acquisition & Pre-processing
### Data Acquisition
#### 주가데이터(KOSPI)
   - yahoo finance 이용하여 특정기간 동안의 기업별 KOSPI 정보를 수집
   - 수집된 정보 중 종가(Close) 데이터만 예측에 사용

   |Enterprise(KS)|Collection Period|
   |------|------|
   |LG Chem, Ltd. (051910.KS)|2020/1/1 ~ 2022/12/31|
   |Hyundai Engineering & Construction Co., Ltd. (000720KS)|2018/1/1 ~ 2021/12/31|
   |Celltrion, Inc. (068270.KS)|2018/1/1 ~ 2021/12/31|
   |Samsung Biologics Co.,Ltd. (207940.KS)|2020/1/1 ~ 2022/12/31|
   |Ncsoft Corporation (036570.KS)|2018/1/1 ~ 2022/12/31|
   |SK hynix Inc. (000660.KS)|2020/1/1~ 2022/12/31|


#### 뉴스데이터 (빅카인즈, https://www.bigkinds.or.kr/)
   - 통합데이터 빅카인즈 이용하여 기업별, 일자별로 기업 관련 뉴스 수집
   - 일자, 제목, 본문 내용 데이터를 예측에 사용



## 🕰️ 개발 기간
- 2023.08.31 ~

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
  

