#include <stdlib.h>
#include <stdio.h>

void flag() {
	char buf[64];
	FILE *f = fopen("flag.txt", "r");
	fgets(buf, 64, f);
	puts(buf);
	exit(0);
}

void bad() {
	char buf[32];
	gets(buf);
	puts(buf);
}

int main() {
	bad();
	return 0;
}
