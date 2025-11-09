
def display_main_menu():
    print("Enter some numbers seperated by commas eg(5,67,57)")
def get_user_input():
    x = input()
    y = x.split(',')
    arr = []
    for z in y:
        arr.append(float(z))
    return arr
def calc_average(num_list):
    return sum(num_list)/len(num_list)
def find_min_max(num_list):
    return [min(num_list),max(num_list)]
def sort_temperature(num_list):
    return(sorted(num_list))
def calc_median_temperature(num_list):
    s = sorted(num_list)
    n = len(num_list)
    if n%2 == 1:
        return s[int(n/2)]
    else:
        y = int(n/2)
        return (s[y]+s[y-1])/2
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    avg = calc_average(num_list)
    min,max= find_min_max(num_list)
    sort = sort_temperature(num_list)
    median = calc_median_temperature(num_list)
    print("Numbers given:", num_list)
    print("Average:", avg)
    print("Minimum:",min)
    print("Maximm:",max)
    print("sorted_temp:",sort)
    print("Median:",median)

if  __name__ == "__main__":
    main()
