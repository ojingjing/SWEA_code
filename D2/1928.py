import base64
def decode_base64(encoded_str):
    decoded_bytes = base64.b64decode(encoded_str)
    return decoded_bytes.decode('utf-8')
t= int(input())

for i in range(t):
    n = input()
    
    decoded_strings = decode_base64(n)

    print(f'#{i+1} {decoded_strings}')

