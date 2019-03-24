#include <stdio.h>

int main(void) {
int c,d,temp;
scanf("%d %d",&c,&d);
temp=c;
c=d;
d=temp;
printf("%d %d",c,d);
	return 0;
}
