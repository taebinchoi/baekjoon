#include <stdio.h>
 
int f[41] = {0,1,1};
int n1 = 0;
int n2 = 0;
 
int fib(int N){
    if (N==1 || N==2){
        n1++;
        return 1;
    }
    else 
        return (fib(N-1) + fib(N-2));
}
 
int fibo(int N){
    for (int i=3; i<=N; i++){
        n2++;
        f[i] = f[i-1] + f[i-2];
    }
    return f[N];
}
 
int main(){
    int N;
    scanf("%d", &N);
    fib(N);
    fibo(N);
    printf("%d %d", n1, n2);
	return 0;
}