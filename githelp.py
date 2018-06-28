#!/usr/bin/env python3

import sys, os


class GitHelp:
    'Git CLI helper for developers'
    cliOptions = {
        'actions': [
            {
                'name':
                'newfeature',
                'description':
                'Create a new feature branch, with some safety checks',
                'handlerFunction':
                'featureBranchHandler',
                'flags': [
                    {
                        'shortForm': 't',
                        'longForm': 'ticket',
                        'description': 'Ticket number',
                        'isRequired': True
                    },
                    {
                        'shortForm': 'f',
                        'longForm': 'feature',
                        'description': 'Short feature description',
                        'isRequired': True
                    },
                    {
                        'shortForm': 'v',
                        'longForm': 'verbose',
                        'description': 'Make output verbose',
                        'isRequired': False
                    },
                ]
            },
        ],
    }

    def __init__(self):
        print("startup")

    def cliHandler(self, args):
        print(args)
        print(self.cliOptions)

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def featureBranchHandler(self, options):
        print("Invoking handler function")
        print(options)


# print(os.popen("git status").read())

if __name__ == '__main__':

    githelp = GitHelp()

    # Get args
    args = sys.argv
    del args[0]

    # Pass to the handler
    githelp.cliHandler(args)

