#include <stdlib.h>
#include <stdio.h>
#include <time.h>

void main(int argc, char **argv) {
	time_t t = time(NULL);
	int sec = atoi(argv[1]);
	srand(t - sec);

	for (int i = 0; i < 30; i++) {
		printf("%d\n", rand() & 0xf);
	}
}