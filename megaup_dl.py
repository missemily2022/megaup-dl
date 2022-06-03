import cloudscraper
from time import sleep

# Accepting MegaUp URL
url = input("Enter your MegaUp URL : ")

client = cloudscraper.create_scraper(allow_brotli=False)
resp = client.get(url)
try:
    data = resp.text.split("DeObfuscate_String_and_Create_Form_With_Mhoa_URL(", 2)[2].split(");")[0].split(",")
except:
    print("Some error occurred while generating direct link. It may be possible that Link is Invalid. Check once again.")
data = [a.strip("' ") for a in data]
time.sleep(3)
idurl = ""
for i in range(int(len(data[0])/4) - 1, -1, -1):
    idurl += data[0][i]
for i in range(int(len(data[0]) / 4 * 3 - 1), int(len(data[0]) / 4 * 2) - 1, -1):
    idurl += data[0][i]
for i in range(int((len(data[1]) - 3) / 2 + 2), 2, -1):
    idurl += data[1][i]
des_url = f"https://download.megaup.net/?idurl={idurl}&idfilename={data[2]}&idfilesize={data[3]}"
des_url = des_url.replace(' ', '%20')
print("Dᴏᴡɴʟᴏᴀᴅ Lɪɴᴋ: ",des_url)