#!/usr/bin/env python3

import sys, os


class GitHelp:
    'Git CLI helper for developers'

    input = {}
    inputRaw = {}

    config = {
        'programInfo': {
            'name': 'githelp',
            'version': 'v0.0.1',
            'shortDesc': 'Git CLI helper for developers',
        },
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
                        'isRequired': True,
                        'val': 'required',
                        'valName': 'tknum',
                        'valExample': 'ba-123',
                    },
                    {
                        'shortForm': 'f',
                        'longForm': 'feature',
                        'description': 'Short feature description',
                        'isRequired': True,
                        'val': 'required',
                        'valName': 'featname',
                        'valExample': 'bootstrap-upgrade',
                    },
                    {
                        'shortForm': 'v',
                        'longForm': 'verbose',
                        'description': 'Make output verbose',
                        'isRequired': False,
                        'val': None,
                        'valName': None,
                        'valExample': None,
                    },
                ]
            },
            {
                'name':
                'status',
                'description':
                'Run git status',
                'handlerFunction':
                'gitStatusHandler',
                'flags': [
                    {
                        'shortForm': 'v',
                        'longForm': 'verbose',
                        'description': 'Make output verbose',
                        'isRequired': False,
                        'val': None,
                        'valName': None,
                        'valExample': None,
                    },
                ]
            },
        ],
    }

    nl = "\n"

    def __init__(self):

        # Validate the configuration options - exits if error
        self.cliValidateConfig()

        # Get args, parse into the class variables
        self.cliParseInput(sys.argv)

        # Validates the input
        # self.cliValidateInput()

        # Pass to the handler
        self.cliHandler(self.inputRaw)

    # Parses the arguments into self.input
    def cliParseInput(self, args):

        # Parse called name of program
        try:
            self.input['callname'] = args.pop(0)
        except IndexError:
            self.input['callname'] = None

        # Parse command
        try:
            self.input['command'] = args.pop(0)
        except IndexError:
            self.input['command'] = None

        # Parse flags - loop through the rest of the arguments
        for i in range(len(args)):
            print("Starting loop to parse flags")

            currentArg = args[i]
            flaginfo = self.cliGetFlagInfo(self.input['command'], currentArg)
            # self.input['flags'] = None

        print(self.input)

    # Validates the configuration options set in self.config
    # Once implemented, run in the constructor
    def cliValidateConfig(self):

        # implement me - check for all required keys in each action, as well as the overall structure
        if False:
            self.showErr("Invalid configuration")

    # Validates the configuration options set
    def cliValidateInput(self):

        # implement me - check for all required keys in each action, as well as the overall structure
        if False:
            self.showErr("Invalid configuration")

    # Show the help page, autogenerated based on settings
    def cliShowHelp(self):
        i = self.config['programInfo']
        actions = self.config['actions']

        # Program name and version
        s = i['name'] + " "
        s += i['version'] + self.nl
        s += i['shortDesc'] + self.nl + self.nl

        s += "Usage: " + i['name'] + " [command] --flag1 --flag2 --flag3=val"
        s += self.nl + self.nl

        s += "Commands available:"
        s += self.nl + self.nl

        # Display the actions
        for a in actions:
            s += "   " + a['name'] + " : "
            s += a['description']

            # Display the flags for the actions
            if len(a['flags']) > 0:
                s += self.nl

            # Nicely display the possible flags
            for f in a['flags']:
                s += "       "

                s += "-" + f['shortForm']

                if f['val'] == 'optional':
                    s += " [<" + str(f['valName']) + ">]"
                elif f['val'] == 'required':
                    s += " <" + str(f['valName']) + "> "

                s += " [OR]"
                s += " --" + f['longForm']

                if f['val'] == 'optional':
                    s += "[=<" + str(f['valName']) + ">]"
                elif f['val'] == 'required':
                    s += "=<" + str(f['valName']) + ">"

                s += "\t  " + f['description']
                if f['isRequired']:
                    s += " (optional)"

                s += self.nl

            if len(a['flags']) > 0:
                s += self.nl
        # Output the help string
        print(s)

    # Returns the full configuration by the action name
    def cliGetActionConfigByName(self, actionName):

        for x in self.config['actions']:
            if x['name'] == actionName:
                print("i found it! " + x['description'])
                return x

        return None

    # Gets flag configuration info by flag name
    def cliGetFlagInfo(self, action, flagstr):
        # First, get the action configuration info, which contains the flags
        actionConfig = self.cliGetActionConfigByName(action)

        for x in actionConfig:
            if "-" + x['shortForm'] == flagStr:
                print("i found the flag (short)! " + x['description'])
                return x
            elif "--" + x['longForm'] == flagStr:
                print("i found the flag (long)! " + x['description'])
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
                return self.showErr("The command '" + action +
                                    "' is not a valid command")

        # Run the handler for the provided action
        getattr(self, actionConfig['handlerFunction'])(actionConfig)

    # Display an error, exit with exit code 1
    def showErr(self, msg):
        print("ERROR: " + msg)
        # print("Run '" + self.config['programInfo']['name'] + " --help' for more info" + self.nl)
        print("Run '" + self.config['programInfo']['name'] +
              "' with no arguments for more info" + self.nl)
        exit(1)

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def featureBranchHandler(self, options):
        print("Invoking feature branch handler with options:")
        print(options)


# Base function for shelling out to system
# print(os.popen("git status").read())

# Init handler
if __name__ == '__main__':

    githelp = GitHelp()
