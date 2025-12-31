#include<stdio.h>
long long count;

int iterativefib(int n){
    count++;
    if(n <= 0) return 0;
    count++;
    if(n == 1) return 1;
    int a = 0, b = 1, c;
    count++;
    for(int i = 2; i <= n; i++){
        count++;
        c = a + b;
        count++;
        a = b;
        count++;
        b = c;
        count++;
    }
    count++;
    return b;
}

int recursivefib(int n){
    count++;
    count++;
    if(n <= 0) return 0;
    count++;
    if(n == 1) return 1;
    count++;
    return recursivefib(n - 1) + recursivefib(n - 2);
}

int main(){
    int n;
    printf("Enter the position of the Fibonacci number to find: ");
    scanf("%d", &n);
    count = 0;
    int result1 = iterativefib(n);
    printf("The result using iterative method is: %d\n", result1);
    printf("The number of operations performed in iterative method: %lld\n", count);

    count = 0;
    int result2 = recursivefib(n);
    printf("The result using recursive method is: %d\n", result2);
    printf("The number of operations performed in recursive method: %lld\n", count);
}