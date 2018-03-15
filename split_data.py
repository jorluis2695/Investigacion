import os, sys
import getopt


def message():
    print('split_data.py --name <file name>')

def main(argv):
    try:
        opts, args = getopt.getopt(argv,'',["name="])
    except getopt.GetoptError:
        print("You need to insert the file name")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "--name":
            name = arg

    file_name, ext =name.split(".")
    if not os.path.exists(file_name):
        os.mkdir(file_name)
    lines_per_file = 1000000
    smallfile = None
    with open(name) as bigfile:
        for lineno, line in enumerate(bigfile):
            if lineno % lines_per_file == 0:
                if smallfile:
                    print('done')
                    smallfile.close()
                small_filename = (file_name+'/'+file_name+'_{}.'+ext).format(int(lineno/lines_per_file))
                smallfile = open(small_filename, "w")
            smallfile.write(line)
        if smallfile:
            smallfile.close()


if __name__ == "__main__":
    main(sys.argv[1:])
