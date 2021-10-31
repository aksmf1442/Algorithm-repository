def main():
    x = int(input())
    
    for i in range(x):
        if i % 2 == 0:
            print("*" * x)
        else:
            print("*")
            

if __name__=="__main__":
    main()