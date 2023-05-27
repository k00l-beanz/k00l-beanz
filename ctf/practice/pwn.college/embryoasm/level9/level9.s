.intel_syntax noprefix
.global _start

_start:
	xor rax, rax
	or rax, 0x1	

	and rdi, 0x1
	xor rax, rdi
