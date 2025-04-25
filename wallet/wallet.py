from ecdsa import SigningKey, VerifyingKey, SECP256k1
import os

PRIVATE_KEY_FILE = "private.pem"
PUBLIC_KEY_FILE = "public.pem"

def generate_keys():
    sk = SigningKey.generate(curve=SECP256k1)
    vk = sk.verifying_key
    return sk, vk

def save_keys(sk, vk):
    with open(PRIVATE_KEY_FILE, "wb") as f:
        f.write(sk.to_pem())
    with open(PUBLIC_KEY_FILE, "wb") as f:
        f.write(vk.to_pem())

def load_keys():
    if os.path.exists(PRIVATE_KEY_FILE) and os.path.exists(PUBLIC_KEY_FILE):
        with open(PRIVATE_KEY_FILE, "rb") as f:
            sk = SigningKey.from_pem(f.read())
        with open(PUBLIC_KEY_FILE, "rb") as f:
            vk = VerifyingKey.from_pem(f.read())
        return sk, vk
    else:
        sk, vk = generate_keys()
        save_keys(sk, vk)
        return sk, vk

def get_public_key_string():
    _, vk = load_keys()
    return vk.to_string().hex()

if __name__ == "__main__":
    print("🔐 Wallet setup complete.")
    print("🪪 Your Miner Address (Public Key):")
    print(get_public_key_string())
