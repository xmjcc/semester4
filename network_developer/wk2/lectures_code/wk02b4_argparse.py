import argparse
import textwrap



parser = argparse.ArgumentParser(
    prog='PROG',                                            # name to display
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
        Please do not mess up this text!
        --------------------------------
            I have indented it
            exactly the way
            I want it
'''))

parser.add_argument(
    'role', 
    help='either server or client')

parser.add_argument(
    '-proto', 
    choices='http tcp udp smtp'.split(),
    help='protopcol to use')

parser.add_argument(
    '-port', '-p',
    default=80,
    type=int,
    help='port to use')
    
args = parser.parse_args()
print(args.role)
print(args.proto)
print(args.port)


# parser = argparse.ArgumentParser(description='Group 1 solution to Lab 5')
# parser.add_argument('--foo', nargs='?', help='foo help')
# parser.add_argument('bar', nargs='+', help='bar help')
