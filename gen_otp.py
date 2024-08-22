import time
import hmac
import hashlib
import base64
import subprocess

def get_secret_key(service_name, username):
    try:
        result = subprocess.run(
            ['security', 'find-generic-password', '-s', service_name, '-a', username, '-w'],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return None

def get_hotp_token(secret, intervals_no):
    key = base64.b32decode(secret, True)
    msg = intervals_no.to_bytes(8, 'big')
    hmac_digest = hmac.new(key, msg, hashlib.sha1).digest()
    
    ob = hmac_digest[19] & 15
    token = (int.from_bytes(hmac_digest[ob:ob + 4], 'big') & 0x7fffffff) % 1000000
    return str(token).zfill(6)

def get_totp_token(secret):
    intervals_no = int(time.time()) // 30
    return get_hotp_token(secret, intervals_no)

username = "kietnt"
secret_key = get_secret_key("vpn_vng_secret", username)
secret_pin = get_secret_key("vpn_vng_pin", username)
otp_code = get_totp_token(secret_key)
print(f'{secret_pin}{otp_code}')
