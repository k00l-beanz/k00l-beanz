# Simple Encryptor

## Recon

Lets see what we're working with:

```bash
file encrypt 
encrypt: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=0bddc0a794eca6f6e2e9dac0b6190b62f07c4c75, for GNU/Linux 3.2.0, not stripped
```

ELF, 64-bit, dynamically linked, not stripped. Ok, nothing crazy. Lets look at the code:


## Code Review

Loading the file into Ghidra and viewing the `main` function and cleaning it up:

```c

undefined8 main(void)

{
  int first_rand;
  time_t current_time;
  long in_FS_OFFSET;
  uint uint_current_time;
  uint second_rand;
  long i;
  FILE *flag_file_handle;
  size_t file_content_size;
  void *file_memory_loc;
  FILE *flag_enc_file_handle;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  flag_file_handle = fopen("flag","rb");
  fseek(flag_file_handle,0,2);
  file_content_size = ftell(flag_file_handle);
  fseek(flag_file_handle,0,0);
  file_memory_loc = malloc(file_content_size);
  fread(file_memory_loc,file_content_size,1,flag_file_handle);
  fclose(flag_file_handle);
  current_time = time((time_t *)0x0);
  uint_current_time = (uint)current_time;
  srand(uint_current_time);
  for (i = 0; i < (long)file_content_size; i = i + 1) {
    first_rand = rand();
    *(byte *)((long)file_memory_loc + i) = *(byte *)((long)file_memory_loc + i) ^ (byte)first_rand;
    second_rand = rand();
    second_rand = second_rand & 7;
    *(byte *)((long)file_memory_loc + i) =
         *(byte *)((long)file_memory_loc + i) << (sbyte)second_rand |
         *(byte *)((long)file_memory_loc + i) >> 8 - (sbyte)second_rand;
  }
  flag_enc_file_handle = fopen("flag.enc","wb");
  fwrite(&uint_current_time,1,4,flag_enc_file_handle);
  fwrite(file_memory_loc,1,file_content_size,flag_enc_file_handle);
  fclose(flag_enc_file_handle);
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}


```

There's a lot happening here so let's break it down:

The first part opens a file, and read it into memory.

```c
flag_file_handle = fopen("flag","rb");
fseek(flag_file_handle,0,2);
file_content_size = ftell(flag_file_handle);
fseek(flag_file_handle,0,0);
file_memory_loc = malloc(file_content_size);
fread(file_memory_loc,file_content_size,1,flag_file_handle);
fclose(flag_file_handle);
```

Then, `srand` is seeded with the current time. The file contents are indexed where some encryption occurs by generating two random numbers.

```c
current_time = time((time_t *)0x0);
uint_current_time = (uint)current_time;
srand(uint_current_time);
for (i = 0; i < (long)file_content_size; i = i + 1) {
first_rand = rand();
*(byte *)((long)file_memory_loc + i) = *(byte *)((long)file_memory_loc + i) ^ (byte)first_rand;
second_rand = rand();
second_rand = second_rand & 7;
*(byte *)((long)file_memory_loc + i) =
        *(byte *)((long)file_memory_loc + i) << (sbyte)second_rand |
        *(byte *)((long)file_memory_loc + i) >> 8 - (sbyte)second_rand;
}
```

`flag.enc` is opened. The time which was used to seed `srand` is written to the first four bytes (probably 32-bit number) of the file. Then the rest of the encrypted flag is written to the file.
```c
flag_enc_file_handle = fopen("flag.enc","wb");
fwrite(&uint_current_time,1,4,flag_enc_file_handle);
fwrite(file_memory_loc,1,file_content_size,flag_enc_file_handle);
fclose(flag_enc_file_handle);
```

## Solving

Since we know the seed that was used for the PRNG, we can generate the two random numbers