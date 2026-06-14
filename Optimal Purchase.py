#flenbar
t = int(input())
for i in range(t):
    n , a , b = map(int,input().split())
    if n >= 3 :
        ind_key = n*a
        gru_key = ((n//3)*b)
        if (n%3)*a > b :
            gru_key += b
        else:
            gru_key += (n%3)*a
        print(min(ind_key,gru_key))
    else:
        ind_key = n*a
        gru_key = b
        print(min(ind_key,gru_key))
