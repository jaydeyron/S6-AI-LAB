//headers and namespaces
#include <bits/stdc++.h>
using namespace std;

//optimization
#pragma GCC optimize ("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

//speedup i/o
#define speedIO ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

//macros
#define endl '\n'
#define llmax LLONG_MAX
#define llmin LLONG_MIN
#define yes cout<<"YES"<<endl
#define no cout<<"NO"<<endl
#define vit vector<long long int>::iterator it;
#define pb push_back
#define vi vector<ll>
#define PI 3.141592653589793238462
#define mod 1000000007

//typedefs
typedef long long ll;
typedef unsigned long long ull;
typedef long double lld;

//global var


//functions


//solution
void solve(){
    lld r,c,d;
    cout<<"Enter returns: ";
    cin>>r;
    cout<<"\nEnter capital: ";
    cin>>c;
    cout<<"\nEnter number of days: ";
    cin>>d;
    cout<<"\n";
    cout<<"Initial capital: "<<c<<"\n";
    for(int i=0;i<d;i++){
        c+=(c*r);
        cout<<"Day "<<i+1<<" capital: "<<c<<"\n";
    }
}

//main
int main() {
    speedIO
    // int t;
    // cin>>t;
    // for(int tt=1;tt<t+1;tt++)
    // {
        //cout<<"Case #"<<tt<<": ";
        solve();
    // }
    return 0;
}