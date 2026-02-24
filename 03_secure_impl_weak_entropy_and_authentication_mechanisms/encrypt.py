#!/usr/bin/env python3

import random
import sys
import time
from Crypto.Cipher import AES
import tqdm

def encrypt(input_file, output_file):
    random.seed(int(time.time()))
    key = random.randbytes(16)
    aes = AES.new(key, AES.MODE_GCM)

    with open(input_file, 'rb') as f_in:
        data = f_in.read()
    ciphertext, tag = aes.encrypt_and_digest(data)

    with open(output_file, 'wb') as f_out:
        f_out.write(aes.nonce)  # 16 bytes
        f_out.write(tag)        # 16 bytes
        f_out.write(ciphertext) # len(data) bytes

def decrypt(encrypt_file, decrypt_output):
    with open(encrypt_file, 'rb') as f_in:
        data = f_in.read()
        nonce = data[:16]
        tag = data[16:32]
        ciphertext = data[32:]

    for e in tqdm.tqdm(range(int(time.mktime((2026, 2, 13, 0, 0, 0, 0, 0, 0))), int(time.mktime((2026, 2, 14, 0, 0, 0, 0, 0, 0))))):
        random.seed(int(e))
        key = random.randbytes(16)
        aes = AES.new(key, AES.MODE_GCM, nonce=nonce)
        try:
            plaintext = aes.decrypt_and_verify(ciphertext, tag)
            with open(decrypt_output, 'wb') as f_out:
                f_out.write(plaintext)
            return
        except ValueError:
            continue

if __name__ == '__main__':
    # if len(sys.argv) != 3:
    #     print(f'usage: {sys.argv[0]} <src-file> <dst-file>', file=sys.stderr)
    #     exit(1)
    # encrypt(sys.argv[1], sys.argv[2])
    decrypt("ciphertext.bin", "plaintext.txt")
