import sys

if 'cbcpipelinefiles' in sys.argv[2].lower():
    print("Arg 1 : {}".format(sys.argv[1].lower()))
    print("Arg 2 : {}".format(sys.argv[2].lower()))
    print("Arg 3 : {}".format(sys.argv[3].lower()))
else:
    print("Mismatch")