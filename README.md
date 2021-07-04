# 먹다 - 먹고싶은거 다있다.<br>
음식 동영상 플랫폼 & 주변 맛집 동영상 <br>
contact us : gkuer95@gmail.com<br><br>

<플랫폼 설명>
점심 뭐먹지? 저녁 뭐먹지? 야식 뭐먹지? <br>
하루 3번하는 고민! 현재 위치 주변 맛집들 영상 보면서 선택하자!<br><br>

현재 자신의 위치 주변에 맛집들의 음식 동영상들이 와르르!<br>
뭐 먹을지 고민하고 있나요? 우리가 도와줄게요.

<br><br><br><br><br>

<개발 설명>
<h3> 1. 로그인 & 회원가입 &</h3>
![스크린샷 2021-07-05 오전 5 13 48](https://user-images.githubusercontent.com/64361457/124398390-6d8cd380-dd50-11eb-9be7-26ab462abfad.png)

<h4> Djnago 기반 제작하였습니다. <br> Social login은 배포하지 않아 적용하지 않았습니다.</h4>

<h3> 2. 동영상 업로드</h3>
![스크린샷 2021-07-05 오전 5 13 48](https://user-images.githubusercontent.com/64361457/124398390-6d8cd380-dd50-11eb-9be7-26ab462abfad.png)

<h4> 1) 가게이름을 검색하는 동안 실시간으로 추천목록이 AutoComplete으로 뜨게하였습니다. key up down으로 감지하여 ajax를 통하여 해당 Inputdata를 view로 전송하였고, view에서는 naver open api를 이용하여 해당 글자에 맞는 검색결과를 끌어와 template으로 전송하였습니다.<br>2) 사용자가 가게이름을 쓰는 동안, 그리고 다 쓴 후, 실시간으로 가게 주소를 가게 주소칸에 value를 바꿔 자동으로 작성되게 하였으며, X좌표와 Y좌표 또한 기입되게 하여 나중에 거리산출에 쓰일 수 있도록 구성하였습니다. 모두 네이버 open api에서 items목록에서 뽑아왔으며, 좌표의 경우에는 네이버는  tm 128(카텍) 좌표를 송출하여 latlng형식으로 바꿔준 뒤 데이터베이스에 저장하였습니다. <br> 3) 동영상 형식만 올릴 수 있도록 파일업로드를 form.py를 통해 제한하였으며, 형식을 모두 채울 경우에만 post되도록 하였습니다.</h4>
![스크린샷 2021-07-05 오전 5 15 29](https://user-images.githubusercontent.com/64361457/124398396-7a112c00-dd50-11eb-8a93-d47edbf6bb7b.png)
![스크린샷 2021-07-05 오전 5 17 35](https://user-images.githubusercontent.com/64361457/124398397-7aa9c280-dd50-11eb-97f7-3695557cee57.png)
![스크린샷 2021-07-05 오전 5 17 46](https://user-images.githubusercontent.com/64361457/124398404-81d0d080-dd50-11eb-96e4-e24d7c30e3bf.png)
![스크린샷 2021-07-05 오전 5 18 02](https://user-images.githubusercontent.com/64361457/124398406-8301fd80-dd50-11eb-98e6-69fb0898691c.png)


<h3> 1. 로그인</h3>
<p align = "center">
<img width="1792" alt="스크린샷 2021-02-02 오후 9 49 26" src="https://user-images.githubusercontent.com/64361457/124398390-6d8cd380-dd50-11eb-9be7-26ab462abfad.png">
</p>
<br><br><br>


<h3> 2. 메인화면 </h3>
<p align = "center">
<img width="1515" alt="스크린샷 2021-02-02 오후 9 51 29" src="https://user-images.githubusercontent.com/64361457/124398396-7a112c00-dd50-11eb-8a93-d47edbf6bb7b.png"></p>
<br><br><br>


<h3> 3. 글작성 </h3>
<p align = "center">
<img width="1792" alt="스크린샷 2021-02-02 오후 9 50 35" src="https://user-images.githubusercontent.com/64361457/124398397-7aa9c280-dd50-11eb-97f7-3695557cee57.png">
</p>
<br><br><br>

<h3> 4. contact us </h3>
<p align = "center">
<img width="1391" alt="스크린샷 2021-02-02 오후 9 51 47" src="https://user-images.githubusercontent.com/64361457/124398404-81d0d080-dd50-11eb-96e4-e24d7c30e3bf.png">
</p>

<h3> 4. contact us </h3>
<p align = "center">
<img width="1391" alt="스크린샷 2021-02-02 오후 9 51 47" src="https://user-images.githubusercontent.com/64361457/124398406-8301fd80-dd50-11eb-98e6-69fb0898691c.png">
</p>
