#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int n;
    float po = 0, ne = 0, ze = 0;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0;arr_i < n;arr_i++){
       cin >> arr[arr_i];
       if(arr[arr_i] > 0)
           po++;
       else if(arr[arr_i] < 0)
           ne++;
       else 
           ze++;
       
    }
    printf("%f\n%f\n%f",po/n,ne/n,ze/n);
    return 0;
}
