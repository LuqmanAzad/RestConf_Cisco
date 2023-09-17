# Interface Configuration
Automation Network Devices

I'd Like to share you some of Python code using RESP API to configure Cisco Interfaces.

# Requirments
- installing Requests Library using this command
```shell
pip install requests
```
- Use Cisco SandBox, GNS3 or any VM network Simulation.
- In Cisco SandBox use CRS1000v router.
- Enable SSHv2 on Router with privilege 15
- Use this command to enable restconf and Accept HTTPS request in Global Configuration.
```shell
ip server
ip secure-server
restconf
```

Now we can run the Python code to do our Configuration.
