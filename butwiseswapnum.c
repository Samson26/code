#include <stdio.h>

int main(void) {
int e,f,temp;
scanf("%d %d",&e,&f);
temp=e;
e=f;
f=temp;
printf("%d %d",e,f);
	return 0;
}
