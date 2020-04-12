import pandas as pd
# 키, 몸무게, 유형 데이터프레임 생성하기

tbl = pd.DataFrame({
    "weight": [ 80.0, 70.4, 65.5, 45.9, 51.2, 72.5 ],
    "height": [ 170,  180,  155,  143,  154,  160  ],
    "gender": [ "f",  "m",  "m",  "f",  "f",  "m"  ]
})
# sap xep ket qua theo chieu cao, khong noi gi tuc la lon dan
print("--- 키로 정렬")
print(tbl.sort_values(by="height"))
# sap xep theo can nang va co yeu cau sap xep nho dan
print("--- 몸무게로 정렬")
print(tbl.sort_values(by="weight", ascending=False)) 
# ascending la sap xep 오름차순 = sai => 내림차순