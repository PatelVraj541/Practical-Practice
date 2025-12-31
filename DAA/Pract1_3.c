#include<stdio.h>
long long count;

int sumrec(int n){
    count++;
    count++;
    if(n == 0) return 0; 
    count++;
    count++;
        return n + sumrec(n - 1);
}

int main(){
    int n, sum;
    printf("Enter a positive integer: ");
    scanf("%d", &n);
    count = 0;
    sum = sumrec(n);
    printf("Sum = %d\n", sum);
    printf("Count = %lld\n", count);
    return 0;
}