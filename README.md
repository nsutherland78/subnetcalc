# subnetcalc
subnetcalc is a simple tool created to allow quick subnet calculations/validations to be performed without outside dependencies.

## Requirements

The host requires the following to run this tool:

* python3
 * argparse
 * ipaddress
 
## To install this tool, simply clone the git repository to a host in the preferred directory:

```
git clone https://github.com/nsutherland78/subnetcalc.git
```

## Usage

Arguments:
```
⇒  subnetcalc -h
usage: subnetcalc.py [-h] [-p PREFIX] network

Calculates subnets

positional arguments:
  network               Enter an IP network in NN.NN.NN.NN/SS,
                        NN.NN.NN.NN/SS.SS.SS.SS or NN.NN.NN.NN/WW.WW.WW.WW
                        notation

optional arguments:
  -h, --help            show this help message and exit
  -p PREFIX, --prefix PREFIX
                        This value specifies the provided networks prefix
                        length to display in the subnetworks output
```

Example usage with a standard network prefix:
```
⇒  subnetcalc 192.168.100.0/24
Network or Host Provided:        192.168.100.0/24
CIDR Notation:                   192.168.100.0/24
Standard Mask:                   192.168.100.0/255.255.255.0
Wildcard Mask:                   192.168.100.0/0.0.0.255
Network and Broadcast IPs:       192.168.100.0, 192.168.100.255
Usable IPs in Network:           192.168.100.1 - 192.168.100.254
Supernet of Network Is:          192.168.100.0/23
/24 Subnetworks Are:
192.168.100.0/25
192.168.100.128/25
```

Example usage specifying custom subnetworks to output:
```
⇒  subnetcalc 192.168.100.0/24 -p 26
Network or Host Provided:        192.168.100.0/24
CIDR Notation:                   192.168.100.0/24
Standard Mask:                   192.168.100.0/255.255.255.0
Wildcard Mask:                   192.168.100.0/0.0.0.255
Network and Broadcast IPs:       192.168.100.0, 192.168.100.255
Usable IPs in Network:           192.168.100.1 - 192.168.100.254
Supernet of Network Is:          192.168.100.0/23
/26 Subnetworks Are:
192.168.100.0/26
192.168.100.64/26
192.168.100.128/26
192.168.100.192/26
```

## Contributors
* Nathan Sutherland (nathan.sutherland@gmail.com)
