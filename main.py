import os, pprint, random, sys


def build_profile(root_dir, depth):
    """
    Traverses the file system starting at the given directory to the given depth
    """
    profile = recursive_profile(root_dir, depth)
    pp = pprint.PrettyPrinter()
    pp.pprint(profile)

def calc_size(directory):
    # TODO: calculate actual size
    return random.randint(1,10)

def recursive_profile(path, current_depth):
    """
    Recursively builds a profile of the given directory
    """
    if current_depth == 0:
        return {}
    else:
        dir_list = [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item)) == True]
        return {
                "name" : path,
                "value" : calc_size(path),
                "children" : [recursive_profile(os.path.join(path, directory), current_depth - 1)
                    for directory in dir_list]
                }


def parse_args():
    """
    Parses command line args
    """

    if len(sys.argv) < 3:
        print "Incorrect usage." # TODO: add usage instructions
        return
    else:
        root_dir = sys.argv[1]
        depth = int(sys.argv[2])

        print "Using '" + root_dir + "' as root directory and profiling to a depth of '"+ str(depth) + "'"

        build_profile(root_dir, depth)

parse_args()
