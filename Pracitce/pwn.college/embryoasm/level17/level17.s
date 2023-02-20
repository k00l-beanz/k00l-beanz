.intel_syntax noprefix
.global _start

_start:
	jmp TARGET
	mov rax, 0
	mov rax, 0
	mov rax, 0
	mov rax, 0
	mov rax, 0
	mov rax, 0
	mov rax, 0
	mov rax, 0
	mov rax, 0
	mov rax, 0
	mov rax, 0
	nop
	nop
TARGET:
	pop rdi
	jmp [0x403000]
