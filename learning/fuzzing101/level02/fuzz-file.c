#include <stdio.h>
#include <stdlib.h>
#include <libexif/exif-data.h>

int main(int argc, char **argv) {
    if (argc < 2) {
        fprintf(stderr, "usage: %s path\n", argv[0]);
        return 2;
    }

    const char *path = argv[1];
    ExifData *ed = NULL;

    ed = exif_data_new_from_file(path);
    if (!ed) {
        fprintf(stderr, "Failed: exif_data_new_from_file\n");
        return 2;
    }

    return 0;
}
