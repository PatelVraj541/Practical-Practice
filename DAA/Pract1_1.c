#include<stdio.h>
long long count;

int sumLoop(int n){
    count++;
    int sum = 0;
    for(int i=1; i<=n; i++){
        count++;
        count++;
        sum += i;
        count++;
    }count++;
    return sum;
}

int main(){
    int a,sum;
    printf("Enter a positive integer: ");
    scanf("%d",&a);
    count = 0;
    sum = sumLoop(a);
    printf("Sum = %d\n",sum);
    printf("Count = %lld\n",count);
}