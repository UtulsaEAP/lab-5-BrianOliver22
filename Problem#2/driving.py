""""
Name: Brian Oliver
lab time: 2/21/2024 4:30
""" 
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
   #write your code here
    assert float((miles_driven/miles_per_gallon)*dollars_per_gallon)
if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    #print your costs here like example below
    #print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10.0):.2f}')
    miles_driven = float(10)
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):.2f}')
    miles_driven = float(50)
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven ):.2f}')
    miles_driven = float(400)
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven ):.2f}')
