# Daily Procedural Map Generator

> __"A customized GitHub Action for Technical Design Portfolio"__

매일 자동으로 절차적 지형(Procedural Map)을 생성하는 봇 레포지토리입니다.
 __자동화(Automation)__ 와 __절차적 콘텐츠 생성(PCG)__ 알고리즘을 학습하고 적용하기 위해 만들었습니다.

## How It Works

__Cellular Automata (셀룰러 오토마타)__ 알고리즘을 사용하여 유기적인 맵을 생성합니다.

1.  __Initialization__: 격자(Grid)에 랜덤하게 벽(⬛)과 바닥(⬜)을 배치합니다.
2.  __Smoothing (Simulation)__: 각 셀의 이웃을 검사합니다.
    * 주변에 벽이 4개 초과라면 -> 해당 셀도 벽이 됩니다.
    * 주변에 벽이 4개 미만이라면 -> 바닥이 됩니다.
3.  __Automation__: GitHub Actions를 통해 매일 아침 9시(KST)에 파이썬 스크립트가 실행되어 아래 섹션을 업데이트합니다.

---

## 💻 Tech Stack
- Language: Python 3.x
- CI/CD: GitHub Actions
- Algorithm: Cellular Automata for Cave Generation
