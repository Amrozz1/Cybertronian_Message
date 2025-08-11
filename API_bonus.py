import requests
file_id = "1_Xcv1O9ytoVmIt00l6JzY5NltTdGuxWS"
dwnld_url = f"https://drive.google.com/uc?export=download&id={file_id}"


words = requests.get(dwnld_url).text
print(words)