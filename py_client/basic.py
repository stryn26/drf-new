import requests

endpoint = "https://httpbin.org/status/200"
#endpoint = "http://httpbin.org/anything"

get_response = requests.get(endpoint) #API -> untuk mendapatkan respon dari httpbin.org

print(get_response.text) # akan menampilkan  text raw yang didapatkan dari endpoint

#kode diatas akan menampilkan hasil response berupa html 

# print(get_response.json())
#kode diatas akan menampilkan response yang telah dirubah menjadi python dict dari response json yang sering digunakan dalam internet
print(get_response.status_code) #ketika mendapatkan data .json() pada python akan mengalami error dikarenakan data tidak dapat digunakan menjadi json, ini karena kita hanya mendapatkan 1 data yaitu 200
