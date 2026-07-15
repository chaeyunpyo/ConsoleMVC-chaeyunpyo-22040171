# ConsoleMVC

반도체 시료 생산·주문관리 콘솔 애플리케이션. Model / Controller / View 계층을 분리한 콘솔 MVC 구조로 구현한다.

## 개요

- 하나의 생산 라인이 시료(샘플)를 하나씩 생산하며, 주문이 들어온 시료에 대해서만 생산이 진행된다.
- 담당자가 콘솔에서 명령을 입력해 시료 등록, 주문 접수/승인/거절, 생산, 출고를 처리한다.
- 데이터는 In-Memory로 관리한다 (영속성 없음).

## 주문 상태 흐름

```
RESERVED --(거절)--> REJECTED
RESERVED --(승인, 재고 충분)--> CONFIRMED --(출고)--> RELEASE
RESERVED --(승인, 재고 부족)--> PRODUCING --(생산 완료)--> CONFIRMED --(출고)--> RELEASE
```

| 상태 | 의미 |
|---|---|
| RESERVED | 주문 접수 |
| REJECTED | 주문 거절 (정상 흐름 제외, 모니터링 제외) |
| PRODUCING | 승인 완료, 재고 부족으로 생산 중 |
| CONFIRMED | 승인 완료, 출고 대기 중 |
| RELEASE | 출고 완료 |

## 메인 메뉴

| 메뉴 | 설명 | 구현 상태 |
|---|---|---|
| 시료 관리 | 시료 등록, 목록 조회, 이름 검색 | 완료 |
| 주문 (접수/승인/거절) | 고객 주문 접수 및 승인·거절 처리 (재고 확인에 따른 CONFIRMED/PRODUCING 분기) | 완료 |
| 모니터링 | 상태별 주문 수 및 시료별 재고 현황 확인 | 준비 중 |
| 출고 처리 | CONFIRMED 상태 주문에 대한 출고 실행 | 준비 중 |
| 생산 라인 | 생산 중인 시료 및 대기 큐(FIFO) 확인, 생산 완료 처리 | 준비 중 |

## 프로젝트 구조

```
console_mvc/
├── model/            # 도메인 엔티티 및 상태(Enum), Repository
│   ├── sample.py
│   ├── order.py
│   ├── production_queue.py
│   └── repository.py
├── controller/        # 메뉴별 흐름 제어, 상태 전이 로직
│   ├── main_controller.py
│   ├── sample_controller.py
│   ├── order_controller.py
│   ├── monitoring_controller.py    # 스텁
│   ├── production_controller.py    # 스텁
│   └── shipping_controller.py      # 스텁
└── view/              # 콘솔 입출력
    └── console_view.py

main.py                # 진입점
tests/                  # pytest 테스트
```

의존 방향: `View → Controller → Model`

## 실행

```bash
python main.py
```

## 테스트

```bash
pytest
```

## 문서

- [PoC1_ConsoleMVC.md](PoC1_ConsoleMVC.md) — PoC 개요 및 상태 흐름
