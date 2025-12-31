#include<stdio.h>
long long count;

int sumeque(int n){
    int sum = n * (n + 1) / 2;
    count++;
    return sum;
}

int main(){
    int n,sum;
    printf("Enter a positive integer: ");
    scanf("%d",&n);
    count = 0;
    sum = sumeque(n);
    printf("Sum = %d\n",sum);
    printf("Count = %lld\n",count);
}