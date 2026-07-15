from console_mvc.controller.main_controller import MainController


class ConsoleView:
    def __init__(self):
        self.controller = MainController()

    def run(self) -> None:
        while True:
            self._print_summary()
            self._print_main_menu()
            choice = input("메뉴 선택> ").strip()

            if choice == "1":
                self._sample_menu()
            elif choice == "2":
                print("[주문 (접수/승인/거절)] 준비 중입니다.")
            elif choice == "3":
                print("[모니터링] 준비 중입니다.")
            elif choice == "4":
                print("[출고 처리] 준비 중입니다.")
            elif choice == "5":
                print("[생산 라인] 준비 중입니다.")
            elif choice == "0":
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 선택해주세요.")

    def _print_summary(self) -> None:
        summary = self.controller.get_summary()
        print("\n=== 시료 생산·주문관리 시스템 ===")
        print(
            f"등록 시료 수: {summary['sample_count']} | "
            f"총 재고: {summary['total_stock']} | "
            f"전체 주문 수: {summary['order_count']} | "
            f"생산라인 대기 건수: {summary['production_queue_count']}"
        )

    def _print_main_menu(self) -> None:
        print("-" * 40)
        print("1. 시료 관리")
        print("2. 주문 (접수/승인/거절)")
        print("3. 모니터링")
        print("4. 출고 처리")
        print("5. 생산 라인")
        print("0. 종료")

    def _sample_menu(self) -> None:
        while True:
            print("\n--- 시료 관리 ---")
            print("1. 시료 등록")
            print("2. 전체 목록 조회")
            print("3. 이름으로 검색")
            print("0. 이전 메뉴로")
            choice = input("선택> ").strip()

            if choice == "1":
                self._register_sample()
            elif choice == "2":
                self._print_samples(self.controller.sample_controller.list_samples())
            elif choice == "3":
                keyword = input("검색할 이름> ").strip()
                self._print_samples(self.controller.sample_controller.search_by_name(keyword))
            elif choice == "0":
                break
            else:
                print("잘못된 입력입니다. 다시 선택해주세요.")

    def _register_sample(self) -> None:
        try:
            sample_id = input("시료 ID (예: S-001)> ").strip()
            name = input("시료명> ").strip()
            avg_production_time = float(input("평균 생산시간 (min/ea)> ").strip())
            yield_rate = float(input("수율 (예: 0.9)> ").strip())
            stock = int(input("초기 재고 수량> ").strip())
        except ValueError:
            print("입력값이 올바르지 않습니다.")
            return

        sample = self.controller.sample_controller.register_sample(
            sample_id, name, avg_production_time, yield_rate, stock
        )
        print(f"시료가 등록되었습니다: {sample.sample_id} ({sample.name})")

    def _print_samples(self, samples) -> None:
        if not samples:
            print("등록된 시료가 없습니다.")
            return
        print(f"{'ID':<10}{'이름':<15}{'평균생산시간':<12}{'수율':<8}{'재고':<8}")
        for s in samples:
            print(f"{s.sample_id:<10}{s.name:<15}{s.avg_production_time:<12}{s.yield_rate:<8}{s.stock:<8}")
