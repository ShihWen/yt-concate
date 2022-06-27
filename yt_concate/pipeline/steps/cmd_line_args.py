import sys
import getopt


def print_usage():
    print('python test.py -c <channel_id> -s <search_word>')

def arg_parse(input):
    short_opts = 'hc:s:'
    long_opts = 'help channel_id= search_word='.split()

    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)

    # print(opts)
    # print(args)

    channel_id = ''
    search_word = ''
    for opt, arg in opts:
        if opt == '-h':
            print_usage()
        elif opt in ('-c', '--channel_id'):
            input['channel_id'] = arg
        elif opt in ('-s', '--search_word'):
            input['search_word'] = arg
    
    if not channel_id or not search_word:
        print('using default channel_id and search_word ')
    




if __name__ == '__main__':
    arg_parse()