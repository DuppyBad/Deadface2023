# Reflections

For this challenge we were given a public key encoded in a seemingly strange encoding system. Doing some reading around on the forum, we discover that it was encoded using Reflected Binary, also known as Gray Code

Whilst researching how it works, I came across this C program on the [wikipedia](https://en.wikipedia.org/wiki/Gray_code)

```C
typedef unsigned int uint;

// This function converts an unsigned binary number to reflected binary Gray code.
uint BinaryToGray(uint num)
{
    return num ^ (num >> 1); // The operator >> is shift right. The operator ^ is exclusive or.
}

// This function converts a reflected binary Gray code number to a binary number.
uint GrayToBinary(uint num)
{
    uint mask = num;
    while (mask) {           // Each Gray code bit is exclusive-ored with all more significant bits.
        mask >>= 1;
        num   ^= mask;
    }
    return num;
}

// A more efficient version for Gray codes 32 bits or fewer through the use of SWAR (SIMD within a register) techniques. 
// It implements a parallel prefix XOR function. The assignment statements can be in any order.
// 
// This function can be adapted for longer Gray codes by adding steps.

uint GrayToBinary32(uint num)
{
    num ^= num >> 16;
    num ^= num >>  8;
    num ^= num >>  4;
    num ^= num >>  2;
    num ^= num >>  1;
    return num;
}
// A Four-bit-at-once variant changes a binary number (abcd)2 to (abcd)2 ^ (00ab)2, then to (abcd)2 ^ (00ab)2 ^ (0abc)2 ^ (000a)2.
```
And also, the lookup table for conversions. Noting that we can use bitmasks, I implemented the GrayToBinary function in python instead, and changed each character in the ciphertext into it's binary representation

```py
def gray_to_binary(n):
    # gray code functions via having consecutive values differ by one bit, we could use a lookup table OR we could use bitshift magic
    mask = n >> 1
    while mask != 0:
        # We invert current bit if the paired bit in the mask is the same
        n ^= mask
        # shift mask along so that we can consider a new bit
        mask >>= 1
    return n
```

Running the full ciphertext through this process, we get output in the form ``0x2d.....n``, which is quite clearly a hexadecimal representation.

Running the result through cyberchef fromhex, we get our prize

```
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC6BS9XGjVPzekcog2rJ4kCmjGx
5FB/Hoeo1pkH13IIFZljH9ODCtvMwPU3mUI4OOe7Syd0myKeXLc+mq2IteqdDgaR
14uHsGYlNbaoA7rF+PfcwVBpye2T/IbIZWnZ54VYeBFC0OY5XdRWTz/q7KgCKqv8
l4ouaNDTDydhKM/QUQIDAQAB
-----END PUBLIC KEY-----

flag{2f1c3d1dac3c4f5b2b38567459d6c430}
```
