## 🤔 뭐 하는 스크립트인가요?
* 쉽게 이미지를 다운스케일링할 수 있는 툴입니다!

## 🤔 어떻게 사용하면 될까요?
- 👆 `pip install pillow tkinter`를 입력하세요!
- ✌️ `py downcaler.py`를 이용하세요!
- 🤠 쉽게 이미지를 다운스케일 하세요!

## 🤔 그냥 다운스케일러 아닌가요?
- 다운스케일할 때 모자이크처리한 것처럼 흐리게 보이는 것이 싫어 제작하였습니다 (모자이크처럼 처리하면 디테일을 살릴 수 있기 때문에 모든 상황에서 `DownscaleEasily`를 사용하는 것이 바람직한 것은 아닙니다)
- ### 예시를 통한 비교
![스크린샷](/examples/choonsik-others.png)
- 일반적인 다운스케일된 사진: `부드럽게 처리되어 있어 디테일이 살아있지만 흐리게 느껴짐`<br><br>
![스크린샷](/examples/choonsik-this.png)
- `DownscaleEasily`로 다운스케일 한 사진: `부자연스럽지만 라인이 보다 선명하게 따짐`<br><br>

## 체인지로그 (Update: 20240710)
- `1.0.0` (20240710) : 프로젝트 시작!
- `1.1.0` (20240710) : 라인이 선명하게 따지도록 다운스케일 방식을 변경 (`Image.LANCZOS` -> `Image.Resampling.NEAREST`)



## 📸 스크린샷
![테스트](/screenshots/main-1.png)
- `메인 화면`의 스크린샷 입니다<br><br>

![테스트](/screenshots/main-2.png)
- `메인 화면`에서 `해상도를 선택하는` 창의 스크린샷 입니다<br><br>

![테스트](/screenshots/done.png)
- `작업 완료` 윈도우의 스크린샷 입니다
