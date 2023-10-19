#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int CHAR_INT_START;
const int SPECIAL_CHARS_SIZE = 5;
const char SPECIAL_CHARS[SPECIAL_CHARS_SIZE] = {' ', '\"', ',', '.', '\''};

vector<bool> sieve(ll n) {
    vector<bool> prime(n+1, true);
    prime[0] = prime[1] = false;
    for (int i = 2; i*i <= n; i++) {
        if (prime[i]) {
            for (int j = i*i; j <= n; j+=i) {
                prime[j] = false;
            }
        }
    }
    return prime;
}

ll find_inverse(ll e, ll phi_n) {
    e = e%phi_n;
    for (int i = 1; i < phi_n; i++) {
        if ((e*i) % phi_n == 1) {
            return i;
        }
    }
    return -1;
}

ll binpow(ll c, ll e, ll mod) {
    c %= mod;
    ll res = 1;
    while (e > 0) {
        if (e & 1)
            res = res * c % mod;
        c = c * c % mod;
        e >>= 1;
    }
    return res;
}

// Creates the table for converting characters into integers.
map<ll, char> get_table() {
    map<ll, char> intToChar;
    ll charInt = CHAR_INT_START;
    for (char c = 'A'; c <= 'Z'; c++) {
        intToChar[charInt++] = c;
    }
    for (int i = 0; i < SPECIAL_CHARS_SIZE; i++) {
        intToChar[charInt++] = SPECIAL_CHARS[i]; 
    }
    return intToChar;
}

void solve() {
    int e, n;
    cin >> e >> n; // >> CHAR_INT_START;
    CHAR_INT_START = 5;
    int m;
    cin >> m;
    vector<int> encrypted(m);
    for (auto &x:encrypted) cin >> x; 

    vector<bool> isPrime = sieve(100000);

    // Find phi(n)
    ll phi_n = -1;
    ll p = -1, q = -1;
    for (int i = 1; i < n+1; i++) {
        if (isPrime[i] && n % i == 0 && isPrime[n/i]) {
            phi_n = (i-1) * (n/i-1);
            p = i; q = n/i;
            break;
        }
    }
    //assert(phi_n != -1);
    
    if (p==-1||q==-1||__gcd((int)phi_n, e) != 1 || (p==q)) {
        cout << "Public key is not valid!";
        return;
    }

    // Find d
    ll d = find_inverse(e, phi_n);
    assert(d != -1);

    // Find mapping from int to char

    // Decrypt message
    vector<char> message;
    vector<int> messageInt;
    map<ll, char> intToChar = get_table();
    for (int i = 0; i < m; i++) {
        int m = binpow(encrypted[i], d, n);
        message.push_back(intToChar[m]);
        messageInt.push_back(m);
    }
    
    cout << p << " " << q << " " << phi_n << " " << d << endl;
    for (auto c:messageInt) cout << c << " ";
    cout << endl;
    for (auto c:message) cout << c;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
    int t = 1;
    //cin >> t;
    while(t--) {
        solve();
    }
}
