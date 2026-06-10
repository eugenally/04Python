

#  모듈 임포트
import time
from datetime import date, datetime, timedelta

# 오늘 날짜 년, 월, 일 출력
today = date.today()
print('오늘날짜', today, today.year, today.month, today.day)

print('='*30)

# 현재사각
dtime =datetime.now()
print('현재시각', dtime)
print('년/월/일', dtime.year, dtime.month, dtime.day)
print('시/분/초/밀리세컨즈', dtime.hour, dtime.minute, dtime.second, dtime.microsecond)

print('='*30)

# 날짜계산1
# 하루를 얻어와서 변수에 저장 => 1day, 0:00:00형식으로 변환
one_day = timedelta(days=1)
yesterday = today - one_day
# 오늘 날짜에서 하루를 더하거나 째서 날짜를 계산할 수 있다.
tomorrow = today + one_day
print('어제와 오늘', yesterday,tomorrow)

# 날짜계산2
#  오늘에서 어제를 빼면 '하루'의 결과가 나옴
date_diff = today - yesterday
print('날짜차이', date_diff)# 결과 : 1day, 0:00:00

# 날짜형식지정
date_str = today.strftime('%Y-%m-%d')
print('형식지정', date_str)

# 크리스마스까지 남은 날짜 계산

X_mas_str = f'{today.year}-12-25'
# str -> datetime타입으로 형식변환
X_mas_datetime = datetime.strptime(X_mas_str,'%Y-%m-%d')
# datetimt -> date타입으로 형식변환
X_mas_date = datetime.date(X_mas_datetime)
# 각 변수의 값과 타입확인
print(X_mas_str, X_mas_datetime, X_mas_date)
print(type(X_mas_str),type(X_mas_datetime),type(X_mas_date))
# 크리스 마스에서 오늘을 빼면 남은 날짜를 계산 할 수 있다.
date_diff = X_mas_date - today
print('크리스마스까지1',date_diff)
print('크리스마스까지2', date_diff.days)