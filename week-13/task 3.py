def show(n):
    if n == 0:  #base case
        return
    if n > 0:
        print(n)
        show(n-1)
show(0)
