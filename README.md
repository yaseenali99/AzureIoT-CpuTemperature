This is a simple Azure edge module which reads the temperature from the CPU of a Raspberry Pi device and sends it up to the IoT Hub.

Development workflow:

1. Start from Azure New IoT Edge solution and create a new python module using this template.
2. Write code for CPU_temperatyre.py file.
3. Modify existing Dockerfile.arm32v7 to include additional linux packages, container entry point etc.
4. Push Module to container registry on Azure clould.
5. Set module in raspberryPi Iot edge device
