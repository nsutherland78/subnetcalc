#!/usr/bin/env python3

'''
This program was written to allow users to calculate IP subnets without the use of external tools.
'''
import ipaddress

#  ArgumentParser passes variables directly into the app
from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser(
        description='Calculates subnets'
    )
    parser.add_argument(
        'network',
        type=str,
        help='Enter an IP network in NN.NN.NN.NN/SS, NN.NN.NN.NN/SS.SS.SS.SS or NN.NN.NN.NN/WW.WW.WW.WW notation'
    )
    parser.add_argument(
        '-p',
        '--prefix',
        type=int,
        help='This value specifies the provided networks prefix length to display in the subnetworks output'
    )
    return parser.parse_args()


ARGS = create_parser()


def main():
    ipnetwork = ARGS.network
    hostrange = list(ipaddress.IPv4Network(ipnetwork).hosts())
    supernet = ipaddress.IPv4Network(ipnetwork).supernet()
    newprefix = ARGS.prefix
    subnetworks = list(ipaddress.IPv4Network(ipnetwork).subnets(new_prefix=newprefix))
    if newprefix is None:
        newprefix = ipaddress.IPv4Network(ipnetwork).prefixlen
    print('Network or Host Provided:        {}'.format(ipnetwork))
    print('CIDR Notation:                   {}'.format(ipaddress.IPv4Network(ipnetwork).with_prefixlen))
    print('Standard Mask:                   {}'.format(ipaddress.IPv4Network(ipnetwork).with_netmask))
    print('Wildcard Mask:                   {}'.format(ipaddress.IPv4Network(ipnetwork).with_hostmask))
    print('Network and Broadcast IPs:       {}, {}'.format(ipaddress.IPv4Network(ipnetwork).network_address, ipaddress.IPv4Network(ipnetwork).broadcast_address))
    print('Usable IPs in Network:           {} - {}'.format(hostrange[0], hostrange[-1]))
    print('Supernet of Network Is:          {}'.format(supernet))
    print('/{} Subnetworks Are:'.format(newprefix))
    for networks in subnetworks:
        print(networks)


if __name__ == '__main__':
    main()
