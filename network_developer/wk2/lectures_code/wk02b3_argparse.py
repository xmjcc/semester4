# filename: wk0b3_argparse.py
# by Narendra for COMP216 (Aug 2020)

# Demonstates how to use the argparse library

import argparse

def foo(args):
    print(f'in foo {args}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'role',                             #name of the mandatory argument
        help='mode to run this program (client/server)'     #more information to the user
    )
    parser.add_argument(
        '-protocol',                        
        required=True,                      #another way to specify mandatory argument
        choices='http smtp tcp udp'.split(),
        help='the protocol to use'
    )
    parser.add_argument(
        '-port', '-p',                      #optional argument
        default=80,
        type=int,
        help='the port to use'
    )
    parser.add_argument(
        '-user', '-u',                      #two ways to specify user
        help='the user name')

    args = parser.parse_args()
    if args.protocol == 'http':
        foo([args.port, args.protocol, args.role])
    elif args.protocol == 'smtp':
        pass                                #call another method
    elif args.protocol == 'tcp':
        pass                                #call another method    
else:
    print('not running as a script')