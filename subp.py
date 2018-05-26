import subprocess


print("$ ping www.baidu.com")
r = subprocess.call(['ping', 'www.baidu.com'])
print('Exit code:', r)
