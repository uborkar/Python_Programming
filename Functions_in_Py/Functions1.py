#funtion with call by value

def my_function(x):
    print("Before modification inside function :",x)
    x=10 # modifys local copy of the value
    print("After modification inside function :", x)

#main
a=5
print("Before function call:", a)
my_function(a)
print("After function call:", a)