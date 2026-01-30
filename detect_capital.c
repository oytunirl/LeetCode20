#include <stdbool.h>
#include <stdio.h>

bool detectCapitalUse(char* word) {
    bool res = true;
    char *ptr = word;

    // first char lowercase
    if (*ptr >= 'a' && *ptr <= 'z') {
        ptr++;
        while (*ptr != '\0') {
            if (*ptr >= 'a' && *ptr <= 'z') {
                ptr++;
            } else {
                res = false;
                break;
            }
        }
    }
    // first char uppercase
    else if (*ptr >= 'A' && *ptr <= 'Z') {
        ptr++;
        // second char uppercase
        if (*ptr >= 'A' && *ptr <= 'Z') {
            while (*ptr != '\0') {
                if (*ptr >= 'A' && *ptr <= 'Z') {
                    ptr++;
                } else {
                    res = false;
                    break;
                }
            }
        }
        // second char lowercase
        else {
            while (*ptr != '\0') {
                if (*ptr >= 'a' && *ptr <= 'z') {
                    ptr++;
                } else {
                    res = false;
                    break;
                }
            }
        }
    }

    return res;
}
