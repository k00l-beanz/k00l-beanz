.intel_syntax noprefix
.global _start

_start:
	mov rax, [rsp]
	mov rbx, [rsp+0x8]
	mov rcx, [rsp+0x10]
	mov rdx, [rsp+0x18]
	
	add rax, rbx
	add rax, rcx
	add rax, rdx

	xor rdx, rdx
	mov rcx, 0x4
	div rcx

	push rax
