import pandas as pd


class DataToExcel:
    def export_to_excel(self):
        data = [{3: 2}, {15: 3}, {16: 1}, {11: 3}, {2: 2}, {6: 3}, {12: 3}, {1: 3}, {18: 1}, {17: 1}, {14: 3}, {8: 2},
                {7: 3}, {5: 3}, {4: 1}, {9: 3}, {13: 3}]

        # 데이터 정리
        cards = []
        counts = []
        for item in data:
            card, count = list(item.items())[0]
            cards.append(card)
            counts.append(count)

        # 데이터프레임 생성
        df = pd.DataFrame({'Card': cards, 'Count': counts})

        # 엑셀 파일로 저장
        df.to_excel('card_backlog.xlsx', index=False)

