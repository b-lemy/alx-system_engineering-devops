### POSTMORTEM ANALYSIS
`DURATION`
1200Hrs - 2300Hrs EAT
- [ ] Failure of one of the server to get requests
Since the loadbalancer used round robin lead to such error
The services could could get requests but some time could returning sites unreachable 
So the service was unreliable so about `50 %` of the users were not able to get the services

#### Root Causes
ThE SERVER inbuilt firewall blocked the port service `8080/tcp` leading to inability to access the port 

#### Timeline
 
`When was the issue detected`
The issue was detected at 1200Hrs.

A customer Complained this is how the issue was detected

Since the services was not withholding the we first moved to the loadbalancer then we inspected the 2 servers where we curled the requests in both serves realizing that on one the serves 

`misleading investigation/debugging paths that were taken`
-[ ] The server needed to be updated
-[ ] Going back to the codebase to check how the end points where configured


`which team/individuals was the incident escalated to`
The Icident was escalated to the Devops 

`how the incident was resolved`
Allowing the ports in the firewalld in the linux server 

`Root cause and resolution must contain:`
The default configuration of firewalld denies every ports so before you enable it you have to allow all ports to should be allowed

```
How the issue was fixed
sudo firewall-cmd --zone=public --add-port=8080/tcp
sudo firewall-cmd --zone=public --list-ports


Output
8080/tcp

```
Corrective and preventative measures must contain:
Before installing any firewall in linux you have to enable the requred ports first the enable it

what are the things that can be improved/fixed (broadly speaking)
-[ ] More knowledge about Linux distros



