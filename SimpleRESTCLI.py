from docopt import docopt
"""Simple Bb REST API CLI v0.0.1
Usage:
  SimpleRESTCLI.py user [USER_ID] [options]
  SimpleRESTCLI.py [options]
  SimpleRESTCLI.py (-h | --help)
  SimpleRESTCLI.py --version
"""
def main():
  pass
if __name__ == '__main__':
  args = docopt(__doc__, version='Elearning DB API 0.0.1')
  debug = args['--debug']
  main()
