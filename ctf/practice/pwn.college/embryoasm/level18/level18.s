.intel_syntax noprefix
.global _start

_start:
	mov eax, dword ptr [rdi]
	cmp eax, 0x7f454c46
	je condition_1
	cmp eax, 0x00005a4d
	je condition_2
	jmp else_condition

condition_1:
	mov eax, dword ptr [rdi+0x4]
	add eax, dword ptr [rdi+0x8]
	add eax, dword ptr [rdi+0xc]
	jmp done

condition_2:
	mov eax, dword ptr [rdi+0x4]
	sub eax, dword ptr [rdi+0x8]
	sub eax, dword ptr [rdi+0xc]
	jmp done

else_condition:
	mov eax, dword ptr [rdi+0x4]
	imul eax, dword ptr [rdi+0x8]
	imul eax, dword ptr [rdi+0xc]
	jmp done

done:		
