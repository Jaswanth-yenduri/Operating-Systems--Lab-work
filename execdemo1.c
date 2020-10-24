#include<stdio.h> 
 #include<stdlib.h>  
#include<unistd.h> 
 int main() 
 {  
 
	char *args[]={"EXEC",NULL};  
	execvp(args[0],args);  
/*All statements are ignored after execvp() call as this wholeprocess(execDemo.c)  
is replaced by another process (EXEC.c) */ 
	printf("Ending-----");  
	return 0; 
 }
