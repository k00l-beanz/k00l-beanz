#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>

int main() {
    time_t t = time(0);
    srand(t);

    long vals[6] = {121, 1231231, 20312312, 122342342, 90988878, 4294967266};

    for (int i = 0; i < 6; i++) {
        int r = rand();
        vals[i] = vals[i] - ((r % 10) + -1);
    }

    int guess = 0;
    for (int i = 0; i < 6; i++) {
        guess = guess + vals[i];
    }

    // Guess
    printf("%d\n", guess);

    return 0;
}