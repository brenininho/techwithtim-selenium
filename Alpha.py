# import datetime
# import calendar
#
# p1 = input(f'Qual país deseja pesquisar ? ')
# m1 = input(f'Qual mẽs ?') # 01
# y1 = input(f'Qual ano ?') # 2020
# import requests
# r = requests.get(f'https://api.covid19api.com/country/{p1}/status/confirmed/live')
# dados = r.json()
# # print(r.status_code)
# # print(pais[0]['Country'])
#
# pais_a = dados[0]['Country']
#
# for item in dados:
#     ultima_dia_do_mes = calendar.monthrange(int(y1), int(m1))[1]
#     tmp_d = ("%s-%s-%s" % (y1, m1.zfill(2), ultima_dia_do_mes))
#     tmp_date      = datetime.datetime.strptime(item['Date'], "%Y-%m-%dT%H:%M:%SZ")
#     tmp_user_date = datetime.datetime.strptime(tmp_d, "%Y-%m-%d")
#
#
#     if tmp_date.strftime("%d/%m/%Y") == tmp_user_date.strftime("%d/%m/%Y"):
#         print(f'No {item["Country"]} no mês {m1} houve {item["Cases"]} casos ')
