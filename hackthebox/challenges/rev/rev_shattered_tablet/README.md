# Shattered Tablet

## Recon

Lets see what we're working with here:
```bash
file tablet 
tablet: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=71ad3ff9f7e5fbf0edc75446337a0a68deb7ecd6, for GNU/Linux 3.2.0, not stripped
```

Seems simple enough. Tossing into Ghidra...

## Code Review

Viewing the `main` code in Ghidra:

```c

undefined8 main(void)

{
  undefined8 local_48;
  undefined8 local_40;
  undefined8 local_38;
  undefined8 local_30;
  undefined8 local_28;
  undefined8 local_20;
  undefined8 local_18;
  undefined8 local_10;
  
  local_48 = 0;
  local_40 = 0;
  local_38 = 0;
  local_30 = 0;
  local_28 = 0;
  local_20 = 0;
  local_18 = 0;
  local_10 = 0;
  printf("Hmmmm... I think the tablet says: ");
  fgets((char *)&local_48,64,stdin);
  if (((((local_28._2_1_ == '4') && (local_38._4_1_ == '3')) && (local_28._4_1_ == 'r')) &&
      ((((local_48._1_1_ == 'T' && (local_38._5_1_ == 'v')) &&
        ((local_48._6_1_ == '0' && ((local_28._7_1_ == '}' && (local_28._6_1_ == 'd')))))) &&
       (local_30._7_1_ == 'r')))) &&
     ((((((local_30._5_1_ == '3' && ((char)local_40 == '3')) && (local_38._6_1_ == 'e')) &&
        ((local_28._3_1_ == '1' && (local_48._5_1_ == 'r')))) &&
       (((char)local_48 == 'H' && (((char)local_28 == '3' && (local_38._2_1_ == '.')))))) &&
      (((((local_40._5_1_ == '4' &&
          (((((local_48._3_1_ == '{' && (local_40._2_1_ == '_')) && ((char)local_38 == '.')) &&
            ((local_48._4_1_ == 'b' && (local_48._7_1_ == 'k')))) && (local_40._7_1_ == 't')))) &&
         (((local_40._6_1_ == 'r' && (local_38._3_1_ == 'n')) &&
          ((local_30._1_1_ == 't' &&
           (((local_38._1_1_ == '.' && (local_40._1_1_ == 'n')) && (local_30._6_1_ == '_')))))))) &&
        (((local_30._2_1_ == '0' && ((char)local_30 == '_')) && (local_40._4_1_ == 'p')))) &&
       ((((local_38._7_1_ == 'r' && (local_30._4_1_ == 'b')) &&
         ((local_28._1_1_ == 'p' &&
          (((local_48._2_1_ == 'B' && (local_30._3_1_ == '_')) && (local_40._3_1_ == '4')))))) &&
        (local_28._5_1_ == '3')))))))) {
    puts("Yes! That\'s right!");
  }
  else {
    puts("No... not that");
  }
  return 0;
}

```

Looks like a headache. I'm a lazy person, so let's use angr. First, install the library in a virtual environment:

```bash
python3 -m venv env
source env/bin/activate
pip3 install angr
```

tbh I don't know a lot about angr but the [documentation](https://docs.angr.io/en/latest/index.html) has improved since the last time I looked at it. I looked up some writeups which use angr and found some good reads:

- https://shivsarthak.medium.com/angr-for-ctf-automating-reversing-a-binary-d5ca574d1d0b
- https://blog.notso.pro/2019-03-20-angr-introduction-part0/

Problem is the API updates frequently so I pulled a script kiddie and slightly copied this dudes [code](https://github.com/angr/angr-examples/blob/master/examples/b01lersctf2020_little_engine/solve.py) which was referenced in the angr documentation.

The script only takes a few seconds to pop the flag:

```bash
python3 solve.py 
WARNING  | 2024-02-21 20:54:37,094 | claripy.ast.bv | BVV value is a unicode string, encoding as utf-8
WARNING  | 2024-02-21 20:54:37,095 | angr.simos.simos | stdin is constrained to 64 bytes (has_end=True). If you are only providing the first 64 bytes instead of the entire stdin, please use stdin=SimFileStream(name='stdin', content=your_first_n_bytes, has_end=False).
b'HTB{br0k3n_4p4rt...n3ver_t0_b3_r3p41r3d}\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
```