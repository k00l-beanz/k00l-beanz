#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {

	char buf[32] = {0};
	strcpy(buf, argv[1]);

	printf("%s\n", &buf);
	return 0;
}
