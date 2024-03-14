# django-backend-youtube
# 1일차
## 프로젝트 세팅
### 1. Github
- 레퍼지토리 생성 => 명령어 그대로 복붙
- 로컬에 있는 내 컴퓨터 폴더와 깃헙의 Remote 공간 연결
- git clone https://github.com/LEE-Hyuna1229/django-backend-youtube
- 모르겠으면 깃헙 데스크탑 프로그램 다운 받기

### 2. Docker Hub
- 회원가입
- 나의 컴퓨터에 가상환경을 구축 (윈도우, 맥 -> 리눅스 환경 구축(MySQL, Python, Redis))
- AcessToken 값을 Github 레퍼지토리에 등록 => 빌드목적

### 3. 장고 프로젝트 세팅
- 실제 배포 환경
- requirements.txt => 실제 배포할 때 사용
- requirements.dev.txt => 개발하고 연습할 때 사용 (파이썬 패키지 관리)
  ex. DRF 버전업 해볼까?
- 실전 : 패키지 의존성 관리 => 버전관리, 패키지들 간의 관계 관리
