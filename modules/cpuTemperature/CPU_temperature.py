import json
#import asyncio
import sys
import time
from gpiozero import CPUTemperature
from azure.iot.device.aio import IoTHubModuleClient

def getTemp():
    cpu = CPUTemperature()
    ts = time.ctime()

    #Build json message
    msg = {
            "Temperature" : cpu.temperature,
            "Timestamp" : ts
            }
    json_msg = json.dumps(msg)
    return json_msg
  

def main():
    #Setup Module client
    module_client = IoTHubModuleClient.create_from_edge_environment()
    
    #Connect the client
    module_client.connect()

    while True:
        temp_json = getTemp()
        module_client.send_message_to_output(temp_json, "output1")
        print(temp_json)
        time.sleep(10)

if __name__ == "__main__":
    main();

