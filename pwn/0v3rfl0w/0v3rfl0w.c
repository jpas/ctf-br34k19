#include <stdlib.h>
#include <stdio.h>

void flag() {
	char buf[64];
	FILE *f = fopen("flag.txt", "r");
	fgets(buf, 64, f);
	puts(buf);
	exit(0);
}

int main() {
	char buf[16];
	gets(buf);
	return 0;
}
