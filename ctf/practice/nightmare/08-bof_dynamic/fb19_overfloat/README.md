# overfloat

First, I'll need to patch the application with the correct version of libc.

```s
$ pwninit --bin overfloat --libc libc-2.27.so 
bin: overfloat
libc: libc-2.27.so

fetching linker
https://launchpad.net/ubuntu/+archive/primary/+files//libc6_2.27-3ubuntu1_amd64.deb
setting ./ld-2.27.so executable
symlinking libc.so.6 -> libc-2.27.so
copying overfloat to overfloat_patched
running patchelf on overfloat_patched
writing solve.py stub
```

Now we can do some basic file enumeration:

```s
$ file overfloat_patched  
overfloat_patched: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter ./ld-2.27.so, for GNU/Linux 2.6.32, BuildID[sha1]=8ae8ef04d2948115c648531ee0c12ba292b92ae4, not stripped
$ pwn checksec overfloat_patched             
[*] 'overfloat_patched'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x3ff000)
    RUNPATH:  b'.'
```

The only notable observation here is that the NX bit is enabled meaning that if we want to get code execution, we'll have to perform a ret2libc.

I throw the patched application into Ghidra. It appears the real meat of this application is in the `chart_course` method.

```c

void chart_course(long target)

{
  int iVar1;
  double dVar2;
  char local_78 [104];
  float user_input;
  uint i;
  
  i = 0;
  do {
    if ((i & 1) == 0) {
      iVar1 = (int)i / 2;
      printf("LAT[%d]: ",
             iVar1 + ((iVar1 / 10 + ((int)(i - ((int)i >> 0x1f)) >> 0x1f)) - (iVar1 >> 0x1f)) * -10)
      ;
    }
    else {
      iVar1 = (int)i / 2;
      printf("LON[%d]: ",
             iVar1 + ((iVar1 / 10 + ((int)(i - ((int)i >> 0x1f)) >> 0x1f)) - (iVar1 >> 0x1f)) * -10)
      ;
    }
    fgets(local_78,100,stdin);
    iVar1 = strncmp(local_78,"done",4);
    if (iVar1 == 0) {
      if ((i & 1) == 0) {
        return;
      }
      puts("WHERES THE LONGITUDE?");
      i = i - 1;
    }
    else {
      dVar2 = atof(local_78);
      user_input = (float)dVar2;
      memset(local_78,0,100);
      *(float *)(target + (long)(int)i * 4) = user_input;
    }
    i = i + 1;
  } while( true );
}


```

The overflow happens at `*(float *)(target + (long)(int)i * 4) = user_input;`. This is because the buffer is a float array with a size of 48. Since each element is 4 bytes long, the buffer should overflow after 15 inputs. I test my theory:

```s
$ ./overfloat_patched
                                 _ .--.        
                                ( `    )       
                             .-'      `--,     
                  _..----.. (             )`-. 
                .'_|` _|` _|(  .__,           )
               /_|  _|  _|  _(        (_,  .-' 
              ;|  _|  _|  _|  '-'__,--'`--'    
              | _|  _|  _|  _| |               
          _   ||  _|  _|  _|  _|               
        _( `--.\_|  _|  _|  _|/               
     .-'       )--,|  _|  _|.`                 
    (__, (_      ) )_|  _| /                   
      `-.__.\ _,--'\|__|__/                  
                    ;____;                     
                     \YT/                     
                      ||                       
                     |""|                    
                     '=='                      

WHERE WOULD YOU LIKE TO GO?
LAT[0]: 1
LON[0]: 1
LAT[1]: 1
LON[1]: 1
LAT[2]: 1
LON[2]: 1
LAT[3]: 1
LON[3]: 1
LAT[4]: 1
LON[4]: 1
LAT[5]: 1
LON[5]: 1
LAT[6]: 1
LON[6]: 1
LAT[7]: 1
LON[7]: 1
LAT[8]: done
BON VOYAGE!
zsh: segmentation fault  ./overfloat_patched
```

And we get a segmentation fault. The next challenge is to determine the offset from the return address.