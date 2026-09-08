import socket

HOST = "143.198.223.223"   
PORT = 30229            

KNOWN_PREFIX = b"JCC{"  

def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))

def get_ciphertext():
    with socket.create_connection((HOST, PORT), timeout=10) as s:
        data = s.recv(4096).decode().strip()
    return bytes.fromhex(data)

def solve():
    c = get_ciphertext()
    print("Ciphertext (hex):", c.hex())

   
    key4 = xor_bytes(c[:4], KNOWN_PREFIX)
    print("Recovered 4-byte key:", key4.hex())

   
    full_key = (key4 * ((len(c) // 4) + 1))[: len(c)]
    flag = xor_bytes(c, full_key)
    print("Flag:", flag)

if __name__ == "__main__":
    solve()
