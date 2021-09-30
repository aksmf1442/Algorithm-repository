def main():
    n = int(input())
    
    for _ in range(n):
        s = input()
        result = "NO"
        for i in s:
            if i != "a":
                result = "YES"
                break
        print(result)
            
        
            

if __name__=="__main__":
    main()