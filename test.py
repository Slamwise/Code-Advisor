# your_script.py
@profile
def main():
    # Generate a list of random numbers
    data = [x**(x+2) for x in range(0,100)]
    print(data)

if __name__ == "__main__":
    main()
