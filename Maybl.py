#include<iostream>
using namespace std;
int main()
{
    int a;
    cout<<"input a"<<endl;
    cin>>a;
    cout<<boolalpha<<(a/100>(a%100)%10)<<endl;
    }
