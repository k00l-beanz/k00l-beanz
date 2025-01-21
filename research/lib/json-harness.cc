#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdint.h>

#define JSON_STATIC
#define JSON_IMPLEMENTATION
#include "json.h"

extern "C" int LLVMFuzzerTestOneInput(const uint8_t *Data, size_t Size) {
        struct json_iter iter;
        struct json_pair pair;

        const char *buf = reinterpret_cast<char*>(const_cast<uint8_t*>(Data));
        iter = json_begin(buf, Size);
        iter = json_parse(&pair, &iter);

        return 0;  // Values other than 0 and -1 are reserved for future use.
}