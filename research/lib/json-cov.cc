#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdint.h>

#define JSON_STATIC
#define JSON_IMPLEMENTATION
#include "json.h"

#define SIZE 100000

int main(int argc, char **argv) {
    
    char input[SIZE] = {0};
    ssize_t length;

    length = read(STDIN_FILENO, input, SIZE);

    struct json_iter iter;
    struct json_pair pair;

    iter = json_begin(input, length);
    iter = json_parse(&pair, &iter);

    return 0;  // Values other than 0 and -1 are reserved for future use.
}