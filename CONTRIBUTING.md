# Contributing to DevKor_Hackathon
DevKor_Hackathon에 관심을 가져주셔서 감사합니다! Contribute를 하기 전에 몇가지 알아두셔야할 점이 있습니다.

## Open Developement
모든 작업은 [GitHub](https://github.com/DevKor-Team/devkor_hackathon_back)에서 이루어집니다. TF를 포함한 이 프로젝트에 참가하는 모든 contributor들은 똑같은 리뷰 프로세스를 거칩니다.

## Branch Oganization
해당 프로젝트는 크게 네가지 종류의 브랜치로 나뉘어 관리됩니다.
* master: 배포
* develop: 개발
* feature: unit 단위의 feature를 개발하여 develop으로 merge할 브랜치
* hotfix: develop에서 급한 bug fix가 필요한 경우

## Bugs
GitHub Issues를 public bug를 찾는데 사용중입니다. 내부적으로 투명하게 버그 수정을 진행합니다. 새로운 작업을 하기 전에 새로운 버그가 생기지 않도록 합니다.

## How to Get in Touch
프로젝트 진행기간(5/1~6/7)동안 slack #데모사이트_오픈에서 관련 논의를 할 수 있습니다.

## Proposing a Change
slack 채널에서 매주 다음주 기획에 대한 제안, 해당 주차 개발사항에 대한 개발 분배가 이루어집니다. 

## Your First Pull Request
프로젝트에 기여하기전, git 심화강의를 듣고 오시는 것을 추천드립니다. 아래 강의도 좋은 선택지중 하나입니다.
[How to Contribute to an Open Source Project on GitHub](https://app.egghead.io/courses/how-to-contribute-to-an-open-source-project-on-github)

## Sending a Pull Request
TF가 pull request를 모니터링중입니다. TF는 pull request들을 리뷰한후, merge하거나, 수정사항을 요청하거나, 설명과 함께 닫을 수 있습니다.
새 api 개발 시, 요청 url과 기능을 요약해 PR에 명시해 주시기 바랍니다.

### Development WorkFlow
*pull request를 날리기 전에, 다음의 것들이 완료돼야 합니다*
1. repository fork 후 develop로부터 feature branch를 만들기
2. repository root에서 `pre-commit install` 실행
3. 만약 code들을 수정 했다면, 각 기능별 요구사항에 맞는지 체크리스트와 함께 테스트를 진행합니다.
### Development environment
* python3가 설치되어 있어야 합니다.
* pip을 통해 requirements.txt의 패키지들이 설치해주세요.
* `python3 manage.py runserver`로 developement server를 시작해주세요

## Style Guide
이 프로젝트에서는 Black라고 하는 automatic code formatter를 사용합니다. 코드를 짠 후에는 `pre-commit run`를 실행해주세요.

이를 실행하지 않더라도 commit 시에 자동으로 검사하게 됩니다. 이때 스타일에 맞지 않은 것이 있을 경우 자동으로 수정되며, 이를 다시 한번 git add 으로 반영한 후 commit 하셔야합니다.
