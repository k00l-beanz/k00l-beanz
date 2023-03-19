#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

int main(int argc, char** argv) {

    char* arguments[101] = {};
    
    for (int i = 0; i < 100; i++) {
        arguments[i] = "A";
    }

    arguments['A'] = "\x00";
    arguments['B'] = "\x20\x0a\x0d";
    arguments[100] = NULL;
    
    execve("./input", arguments, NULL);
    sleep(1);

    const char* stdout = "\x00\x0a\x00\xff";
    write(0, stdout, sizeof(stdout));

    const char* stderr = "\x00\x0a\x02\xff";
    write(2, stderr, sizeof(stderr));

    return 0;
}