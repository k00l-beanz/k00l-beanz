#!/usr/bin/env python3

encrypted_flag = b""
encrypted_flag += b"?"
encrypted_flag += b"d"
encrypted_flag += b"5"
encrypted_flag += b"\f"
encrypted_flag += b"H"
encrypted_flag += b"G"
encrypted_flag += b"\x05"
encrypted_flag += b"o"
encrypted_flag += b"F"
encrypted_flag += b"\x04"
encrypted_flag += b"o"
encrypted_flag += b"\x02"
encrypted_flag += b"\x04"
encrypted_flag += b"\x03"
encrypted_flag += b"\x13"
encrypted_flag += b"("
encrypted_flag += b"R"
encrypted_flag += b"\x0e"
encrypted_flag += b"("
encrypted_flag += b"X"
encrypted_flag += b"C"
encrypted_flag += b"\x0f"
encrypted_flag += b"\0"
encrypted_flag += b"\x05"
encrypted_flag += b"V"
encrypted_flag += b"M"

def decrypt(key: list):
    chars = []
    for i in range(len(encrypted_flag)):
        bv = bytes([encrypted_flag[i]])
        res = bytes([a ^ b for a,b in zip(bv, key[i % 3])])
        chars.append(res)

    try:
        flag = ''.join([byte.decode('utf-8') for byte in chars])
        return flag
    except UnicodeDecodeError:
        return ""
    

def main()-> None:

    
    for i in range(256):
        for j in range(256):
            for k in range(256):
                flag = decrypt([bytes([i]), bytes([j]), bytes([k])])
                if flag.startswith("HTB{"):
                    print(flag)
                    exit(0)
 
    return

if __name__ == "__main__":
    main()