This script is based on the hyundai_kia_connect_api. I created this script so that I would not have to install homeassistant, just to be able to get to the data that my vehicle sends to the cloud anyway.
I wanted to have a way to get the exact percentage of my 12-volt auxiliary battery, something that Kia Connect does not tell you.
Of course, you can simply extend this script to include other information that is contained in the "Vehicle" object if you like, just add the corresponding print statements.

I might make a streamlit app out of this later, if I get the urge :)

You can also modify the relevant Region information in the script if your vehicle is not in the EU, and you can also use it for Hyundai and Genesis vehicles.
There might be limitations however, that come from the API. 
You can check out that repo here: https://github.com/Hyundai-Kia-Connect/hyundai_kia_connect_api

The Hyundai Kia Connect API supports several region and brand options. Here are the available options:

Regions:
1: Europe
2: Canada
3: USA
4: China
5: Australia

Brands:
1: Kia
2: Hyundai
3: Genesis (only available in Canada)
To use these options, you would typically instantiate the VehicleManager class with the appropriate region and brand integers. For example:

vm = VehicleManager(region=2, brand=1, username="username@gmail.com", password="password", pin="1234")
In this example, region=2 refers to Canada, and brand=1 refers to Kia.


