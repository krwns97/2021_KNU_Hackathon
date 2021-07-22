# 2021_KNU_Hackathon

## 📝 문제점 인식
  <p align="center"><img src="https://user-images.githubusercontent.com/59030198/126649011-de272dad-7dbd-4c84-93bb-cb139b218196.png"></p> 
  
   - 현재 경북대학교 모든 건물은 QR 코드 혹은 NFC 태깅을 통해 출입을 허용하고 있으며, 이는 코로나방역의 방문기록으로도 활용된다. 
   하지만, 많은 학생들이 몰리는 특정 시간 때, 한명이 QR코드 인식 후 문이 열리면, 뒤 따르는 수많은 인원이 같이 들어가는 문제점이 존재한다.
   
   - 이는 방문기록에 남겨지지 않아, 만약 교내 확진자가 발생하였을 때 접촉자를 찾는데 어려움을 겪을 수 있다.
   
   ####  => 블루투스 주소를 통한 건물 출입을 제어 / 건물 입구를 지나는 모든 블루투스 주소를 수집하여 DB에 저장하는, 비접촉 방식의 ***건물 출입 시스템*** 을 제안한다. 
   
## 🚀 시스템 구성도 & Sequence diagram
![AI_Hackathon](https://user-images.githubusercontent.com/59030198/126280274-d7fa1989-df9d-483f-a949-1afcdea1f726.png)

시스템은 전체적으로 라즈베리파이와 AWS, 그리고 DB로 구성된다.

 - 백엔드는 AWS에서 Node.js
 - DB는 mongoDB를 사용
 - 하드웨어는 라즈베리파이 OS가 설치된 라즈베리파이 4B와 PIR센서로 구성
((데모를 위한 LED는 개폐장치를 시연하기 위한 구성 외의 품목이다.))

일반적인 장치의 블루투스 연결 거리는 10~20m이다. 따라서 단독으로 사용할 경우 원거리에서 의도치 않게 문이 개방될 수 있다. 보안을 증강하고, 시스템을 더욱 정밀하고 의도한 대로 작동시키기 위해 인체감지센서를 보조로 사용하였으며, 해당 센서의 감지거리를 2m로 조절하여 사용하였다.

 - 사람이 출입구에 접근하면 PIR센서가 이를 감지한다.
 - 리즈베리파이에 내장된 블루투스는 항상 가동되며, 인체감지센서가 사람의 접근을 감지하는 시점에 탐색되는 모든 블루투스 ID를 서버로 전송한다.
 - 서버는 라즈베리파이로부터 받은 블루투스 ID를 DB와 대조하여 학내 구성원 여부를 파악한다.
 - - 학내 구성원임을 식별하면, DB에 시간과 장소 등을 포함하는 로그를 남기고, 통과 허용 신호를 라즈베리 파이로 전송한다.
 - - 만약, 구성원이 아니라면, 블루투스 ID는 서버로그에만 남게 되고, 통과 금지 신호를 라즈베리파이로 전송한다. 
 - 라즈베리파이는 서버로부터 받은 신호를 식별하여 상황에 맞게 문을 개방한다.


## Usecase diagram

## ✨ 시연영상

## 🤝 기대효과
우선, 본 시스템을 통하여 상기한 문제인 수많은 인원이 동시에 인증없이 통과하여 교내 전염병 확진자가 발생하였을 경우 동선 파악과 접촉자 확인의 어려움을 덜어줄 수 있다. 건물의 입장시간 뿐 아니라 상대적으로 관리가 쉽지 않았던 퇴장시간까지 일괄적으로 관리할 수 있어 감염자 파악에 더 많은 기여를 할 것으로 보인다.

아울러, QR코드와 NFC 태깅으로 인증하는 별도의 절차가 필요없어 편의성을 제공한다. 휴대폰을 소지하고 있는 것만으로도 문이 자동으로 개방되므로 QR코드 생성과 같은 번거로운 행동이 필요없어진다. 또한, 건물 내부에서 나올때에도 버튼을 누르는 등의 불필요한 작업 없이 문을 열고 나오면 된다. 접촉이 줄어들게 되므로 감염 예방효과도 더해진다.

## 👤 팀원 정보 및 역할분담
학번 | 소속 | 이름 | 담당업무
----- | ----- | -----
2016112912 | 심화컴퓨터공학 | 박준호 | Bluetooth detect 및 Data 전송
2016114566 | 심화컴퓨터공학 | 이형건 | 적외선 감지 및 하드웨어 구성
2016117003 | 심화컴퓨터공학 | 장현수 | DB 및 백엔드 구성
2019116859 | 글로벌SW융합 | 김미소 | 영상편집

