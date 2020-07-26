# zoozooclub

## colaboratory와 구글 드라이브 연동하기

주피터 노트북에서 해당 코드를 실행한다.
```
from google.colab import drive
drive.mount('/gdrive', force_remount=True)
```
실행 후, 나오는 링크를 따라 들어가서 구글 로그인을 한다.<br>
로그인 후, 나오는 인증 코드를 output 부분에 입력하면 연결 완료!

주피터 노트북에서 아래 명령으로 구글 드라이브의 파일 목록을 확인할 수 있다.
```
!ls "/gdrive/My Drive"
```

---

### 참고
구글 드라이브의 설정을 확인하자.<br>
구글 드라이브 > 설정 > 업로드 변환<br>
에서 업로드 변환이 꺼져있는지 확인해야한다.<br>
업로드하는 파일이 문서로 변하지 않으려면 체크해제를 해야한다.
