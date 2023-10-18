#include <iostream>
#include <vector>
#include <cmath>

using namespace std;
int fastmod(int base,int exponent, int modulo){
    if (exponent == 1)
        return base%modulo;
    if (exponent%2 == 0){
        base = base % modulo;
        return fastmod(pow(base,2),(exponent/2), modulo)%modulo;
    }
    if (exponent%2 == 1){
        base = base % modulo;
        return (base*fastmod(pow(base,2),(exponent/2), modulo))%modulo;
    }
    return -1;
}

bool isPrime(int n) 
{  
    if (n <= 1) 
        return false; 

    for (int i = 2; i < n; i++) 
        if (n % i == 0) 
            return false; 
  
    return true; 
} 

int dumbmodinverse(int number,int modulo){
    for(int i = 1;10000; i++){
        if((i*number)%modulo == 1)
            return i;
    }
    return 0;
}

int gcd (int a, int b){
    if (b == 0)
        return a;
    return gcd(b, a%b);
}
int main(){
    int e, n, m, p, q, phi, d, temp;
    vector<int> message;
    cin >> e;
    cin >> n;
    cin >> m;
    for (int i = 0; i < m; i++){
        cin >> temp;
        message.push_back(temp);
    }
    for(int i = 3; i <= sqrt(n); i+=2){
        if (n%i == 0){
            p = i;
            q = n/i;
            break;
        }
    }
    phi = (p-1)*(q-1);
    if (gcd(e,phi) != 1 || p == q || !isPrime(p) || !isPrime(q)){
        cout << "Public key is not valid!" << endl;
        return 0;
    }
    d = dumbmodinverse(e,phi);
    for (auto &i:message)
        i = fastmod(i,d,n);
    cout << p << " " << q << " " << phi << " " << d << endl;
    for (auto i: message){
        cout << i << " ";
    }
    cout << endl;
    for (auto i: message){
        if(i == 31)
            cout << " ";
        else if (i == 32)
            cout << "\"";
        else if (i == 33)
            cout << ",";
        else if (i == 34)
            cout << ".";
        else if (i == 35)
            cout << "\'";
        else
            cout << (char)(i+60);
    }
    return 0;
}