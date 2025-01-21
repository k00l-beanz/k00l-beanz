#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, char **argv) {
	uint8_t name_length = -1;
	printf("name_length as uint8_t: %hhu\n", name_length);

	int8_t new_name_length = (int8_t) name_length;
	printf("name_length as int8_t: %hhd\n", new_name_length);

	char c = '0';
	printf("%d\n", isalpha(c));

	return 0;
}
