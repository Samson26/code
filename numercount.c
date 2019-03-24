#include<stdio.h>
#include<ctype.h>
int main()
{
int i; 
 int no=0;
char s[100];
scanf("%s",s);
for(i=0;s[i]!='\0';i++)
{
	
if(isdigit(s[i]))
{
no++;
}
}
printf(no);
}
