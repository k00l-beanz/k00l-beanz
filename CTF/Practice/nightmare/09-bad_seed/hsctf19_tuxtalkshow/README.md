# tuxtalkshow

Start with some basic file enumeration

```s
$ file tuxtalkshow 
tuxtalkshow: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=8c0d2b94392e01fecb4b54999cc8afe6fa99653d, for GNU/Linux 3.2.0, not stripped
$ pwn checksec tuxtalkshow 
[*] 'tuxtalkshow'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

Seems like traditional exploitation will be difficult but not impossible.

Lets look at the `main` in Ghidra:

```c

undefined8 main(void)

{
  int random_number;
  time_t time_;
  basic_ostream *pbVar1;
  long in_FS_OFFSET;
  int user_input;
  int i;
  int endgame;
  int j;
  undefined4 local_280;
  undefined4 local_27c;
  undefined4 local_278;
  undefined4 local_274;
  undefined4 local_270;
  undefined4 local_26c;
  int local_268 [8];
  basic_string local_248 [32];
  basic_istream local_228 [520];
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  std::basic_ifstream<char,std::char_traits<char>>::basic_ifstream((char *)local_228,1056944);
  time_ = time((time_t *)0x0);
  srand((uint)time_);
                    /* try { // try from 0010127e to 001012c0 has its CatchHandler @ 00101493 */
  pbVar1 = std::operator<<((basic_ostream *)std::cout,"Welcome to Tux Talk Show 2019!!!");
  std::basic_ostream<char,std::char_traits<char>>::operator<<
            ((basic_ostream<char,std::char_traits<char>> *)pbVar1,
             std::endl<char,std::char_traits<char>>);
  std::operator<<((basic_ostream *)std::cout,"Enter your lucky number: ");
  std::basic_istream<char,std::char_traits<char>>::operator>>
            ((basic_istream<char,std::char_traits<char>> *)std::cin,&user_input);
  local_280 = 121;
  local_27c = 1231231;
  local_278 = 20312312;
  local_274 = 122342342;
  local_270 = 90988878;
  local_26c = 4294967266;
  local_268[0] = 121;
  local_268[1] = 1231231;
  local_268[2] = 20312312;
  local_268[3] = 122342342;
  local_268[4] = 90988878;
  local_268[5] = 4294967266;
  for (i = 0; i < 6; i = i + 1) {
    random_number = rand();
    local_268[i] = local_268[i] - (random_number % 10 + -1);
  }
  endgame = 0;
  for (j = 0; j < 6; j = j + 1) {
    endgame = endgame + local_268[j];
  }
  if (endgame == user_input) {
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string();
                    /* try { // try from 00101419 to 00101448 has its CatchHandler @ 0010147f */
    std::operator>>(local_228,local_248);
    pbVar1 = std::operator<<((basic_ostream *)std::cout,local_248);
    std::basic_ostream<char,std::char_traits<char>>::operator<<
              ((basic_ostream<char,std::char_traits<char>> *)pbVar1,
               std::endl<char,std::char_traits<char>>);
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
              ((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_248);
  }
  std::basic_ifstream<char,std::char_traits<char>>::~basic_ifstream
            ((basic_ifstream<char,std::char_traits<char>> *)local_228);
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}


```

Looks like we have to input a number, some arithmetic happens to it, and then our input needs equivalate the output. The catch is that the number is randomly generated everytime. Because the PRNG is generated with current time, we'll be able to predict each one of these numbers. I wrote a simple C program which will generate the `guess` for us:

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>

int main() {
    time_t t = time(0);
    srand(t);

    long vals[6] = {121, 1231231, 20312312, 122342342, 90988878, 4294967266};

    for (int i = 0; i < 6; i++) {
        int r = rand();
        vals[i] = vals[i] - ((r % 10) + -1);
    }

    int guess = 0;
    for (int i = 0; i < 6; i++) {
        guess = guess + vals[i];
    }

    // Guess
    printf("%d\n", guess);

    return 0;
}
```

Compile and run:

```s
$ ./guess | ./tuxtalkshow
```