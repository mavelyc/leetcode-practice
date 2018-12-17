//how to randomize array in C
#include <stdio.h>
#include <stdlib.h> 

int randomize(int *arr){
    //len of arr
    int len = sizeof(arr)/sizeof(arr[0]);


    return len;
};


int main(){
    int arr[3] = {7,5,6};
    int fin = randomize(arr);
    printf("%d",fin);
}
