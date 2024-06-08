import getpass
from hyundai_kia_connect_api import VehicleManager

def get_user_credentials():
    username = input("Enter your Kia UVO username: ")
    password = getpass.getpass("Enter your Kia UVO password: ")
    return username, password

def main():
    username, password = get_user_credentials()
    
    # Initialize the VehicleManager for the EU region and Kia brand
    region = 1  # Region for Europe
    brand = 1  # Brand for Kia
    pin = ""  # Assuming pin is not required for EU
    
    vm = VehicleManager(region=region, brand=brand, username=username, password=password, pin=pin)
    
    # Authenticate and initialize the vehicle manager
    try:
        vm.initialize()
        print("Login successful!")
    except Exception as e:
        print(f"Failed to login: {e}")
        return
    
    # Retrieve and print vehicle information
    try:
        vm.update_all_vehicles_with_cached_state()
        for vehicle_id in vm.vehicles:
            vehicle = vm.get_vehicle(vehicle_id)
            print_vehicle_info(vehicle)
    except Exception as e:
        print(f"Failed to retrieve vehicle information: {e}")

def print_vehicle_info(vehicle):
    print("Vehicle Information:")
    print(f"Model: {vehicle.model}")
    print(f"Name: {vehicle.name}")
    print(f"VIN: {vehicle.VIN}")
    print(f"Odometer: {vehicle._odometer_value} {vehicle._odometer_unit}")
    aux_battery_level = vehicle.data.get('Electronics', {}).get('Battery', {}).get('Level', 'N/A')
    
    print(f"12V Battery Level: {aux_battery_level}%")
    print(f"Battery Level: {vehicle.ev_battery_percentage}%")

    print(f"Last Update: {vehicle.last_updated_at}")
    print("")

if __name__ == "__main__":
    main()
