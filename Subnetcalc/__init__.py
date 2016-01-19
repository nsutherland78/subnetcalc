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
        '-n',
        '--newprefix',
        type=int,
        help='This value specifies the size of the subnetworks to display in a network'
    )
    return parser.parse_args()

ARGS = create_parser()


def main():
    ipnetwork = ARGS.network
    hostrange = list(ipaddress.IPv4Network(ipnetwork).hosts())
    supernet = ipaddress.IPv4Network(ipnetwork).supernet()
    newprefix = ARGS.newprefix
    subnetworks = list(ipaddress.IPv4Network(ipnetwork).subnets(new_prefix=newprefix))
    print('Network or Host Provided:        {}'.format(ipnetwork))
    print('Network and Broadcast Addresses: {}, {}'.format(ipaddress.IPv4Network(ipnetwork).network_address, ipaddress.IPv4Network(ipnetwork).broadcast_address))
    print('CIDR Notation:                   {}'.format(ipaddress.IPv4Network(ipnetwork).with_prefixlen))
    print('Standard Mask:                   {}'.format(ipaddress.IPv4Network(ipnetwork).with_netmask))
    print('Wildcard Mask:                   {}'.format(ipaddress.IPv4Network(ipnetwork).with_hostmask))
    print('First to Last Host in Subnet:    {} - {}'.format(hostrange[0], hostrange[-1]))
    print('Supernet of network is:          {}'.format(supernet))
    print('Subnetworks are:                 {}'.format(subnetworks))
    # for networks in subnetworks:
    #     print('                                 {}'.format(networks))

if __name__ == '__main__':
    main()
