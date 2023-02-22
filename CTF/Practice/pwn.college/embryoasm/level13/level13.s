.intel_syntax noprefix
.global _start

_start:
	mov rax, [rdi]
	mov rbx, [rdi + 0x8]
	add rax, rbx
	mov [rsi], rax
