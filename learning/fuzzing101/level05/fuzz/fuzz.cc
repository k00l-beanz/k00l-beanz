#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdint.h>


#include "libxml/parser.h"
#include "libxml/tree.h"

using namespace std;

extern "C" int LLVMFuzzerTestOneInput(const uint8_t *Data, size_t Size) {
    xmlDocPtr doc;
    const char *content = (const char*) Data;

    doc = xmlReadMemory(content, Size, "blah.xml", NULL, 0);
    if (doc == NULL) {
        fprintf(stderr, "Failed to parse document\n");
        return 2;
    }

    xmlFreeDoc(doc);

    return 0;
}