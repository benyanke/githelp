#!/usr/bin/env python3

import sys, os


class GitHelp:
    'Git CLI helper for developers'
    cliOptions = {
        'actions': [
            {
                'name': 'newfeature',
                'description': 'Create a new feature branch, with some safety checks',
                'handlerFunction': 'featureBranchHandler',
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


    def cliShowHelp(self):
        print("HELP PAGE")

    # Returns the full configuration by the action name
    def cliGetActionConfigByName(self, actionName):

        for x in self.cliOptions['actions']:
            if x['name'] == actionName:
                print("i found it! " + x['description'])
                return x

        return None


    # Initial entrypoint for CLI usage
    def cliHandler(self, args):

        # Display help info if no params are provided
        if len(args) == 0:
            return self.cliShowHelp()

        # Get the config info for the provided action
        else:
            action = args[0]
            actionConfig = self.cliGetActionConfigByName(action)
            if actionConfig is None:
                return self.showErr("The command '" + action + "' is not a valid command")

        # Run the handler for the provided action
        getattr(self, actionConfig['handlerFunction'])(actionConfig)

    # Display an error, exit with exit code 1
    def showErr(self, msg):
        print("ERR: " + msg)
        exit(1)

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def featureBranchHandler(self, options):
        print("Invoking feature branch handler with options:")
        print(options)


# print(os.popen("git status").read())

if __name__ == '__main__':

    githelp = GitHelp()

    # Get args
    args = sys.argv
    del args[0]

    # Pass to the handler
    githelp.cliHandler(args)

