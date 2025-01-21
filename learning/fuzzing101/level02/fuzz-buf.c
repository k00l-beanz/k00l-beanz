#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <libexif/exif-data.h>

#define MAX_SIZE 100000

int main(int argc, char **argv) {
    if (argc < 1) {
        fprintf(stderr, "usage: %s\n", argv[0]);
        return 2;
    }


    char input[MAX_SIZE] = {0};
    ssize_t length = read(STDIN_FILENO, input, MAX_SIZE);
    ExifData *ed = NULL;

    ed = exif_data_new_from_data((const unsigned char*) input, length);

    if (!ed) {
        fprintf(stderr, "Failed: exif_data_new_from_file\n");
        return 2;
    }

    return 0;
}
