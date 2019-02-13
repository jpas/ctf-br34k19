#include <stdio.h>

int learn() {
    char skill[64];
    gets(skill);
    return skill[0] != '\0';
}

int main() {
    do {
        puts("What would you like to learn?");
    } while (learn());
}
