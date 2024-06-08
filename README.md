This script is based on the hyundai_kia_connect_api. I created this script so that I would not have to install homeassistant, just to be able to get to the data that my vehicle sends to the cloud anyway.
I wanted to have a way to get the exact percentage of my 12-volt auxiliary battery, something that Kia Connect does not tell you.
Of course, you can simply extend this script to include other information that is contained in the "Vehicle" object if you like, just add the corresponding print statements.

I might make a streamlit app out of this later, if I get the urge :)

You can also modify the relevant Region information in the script if your vehicle is not in the EU, and you can also use it for Hyundai and Genesis vehicles.
There might be limitations however, that come from the API. 
You can check out that repo here: https://github.com/Hyundai-Kia-Connect/hyundai_kia_connect_api


