# your_script.py
import random
@profile
def main(n):
    # Generate a list of random numbers
    x_list = []
    y_list = []
    z_list = []
    xyz_list = []
    for x in range(1, n):

        y = x^2
        z = y/random.randint(1, x)

        x_list.append(x)
        y_list.append(y)
        z_list.append(z)


        xyz_list.append((x, y, z))

    print(xyz_list)
if __name__ == "__main__":
    main(100000)
