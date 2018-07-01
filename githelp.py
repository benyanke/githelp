#!/usr/bin/env python3

import sys, os


class GitHelp:
    'Git CLI helper for developers'

    DEBUG = False

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
        ],
    }

    nl = "\n"

    def __init__(self, args):

        # Validate the configuration options - exits if error
        self.cliValidateConfig()

        # Get args, parse into the class variable self.input
        self.cliParseInput(args)

        # Validates the input
        self.cliValidateInput()

        # Pass to the handler
        self.cliHandler()

    def cliParseInput(self, args):
        """ Parses the arguments into self.input

        """

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

        self.input['flags'] = []

        # Insert the flags on to the array
        for i in range(len(args)):

            # Will backtrack and insert the values later
            if args[i].startswith("--"):

                splitArg = args[i].split("=")

                try:
                    self.input['flags'].append({'flag': splitArg[0], 'value': splitArg[1]})
                except IndexError:
                    self.input['flags'].append({'flag': splitArg[0], 'value': None})

            elif args[i].startswith("-"):
                self.input['flags'].append({'flag': args[i], 'value': None})

            elif args[i-1].startswith("-") and not args[i-1].startswith("--"):
                lastFlag = self.input['flags'].pop()
                self.input['flags'].append({'flag': lastFlag['flag'], 'value': args[i]})

            else:
                if self.DEBUG:
                    print("PARSE ERROR")
                self.showErr("Can not provide multiple values for one flag")


        if self.DEBUG:
            print("Parsed input:\n" + str(self.input))

    def cliValidateConfig(self):
        """" Validates the configuration options set in self.config
        Once implemented, run in the constructor
        """

        # implement me - check for all required keys in each
        # action, as well as the overall structure
        # also check to make sure each action has a handler
        # function defined, and that function also exists
        if False:
            self.showErr("Invalid configuration")

    def cliValidateInput(self):
        """Validates the configuration options set
        """

        # implement me - check to ensure that
        # 1) action provided is a valid action
        # 2) all flags found are valid flags for the action
        # 3) all required flags exist
        # 4) all flags with a required value have a value
        # 5) all flags with no value specified do not have one

        # If no command is set, exit validation - this
        # is when we display help screen.
        if self.input['command'] == None:
            return

        # Check to ensure a valid command
        if not self.cliDoesActionExist(self.input['command']):
            self.showErr("'" + self.input['command'] + "' is not a valid command.")

        # Ensure all flags are valid for the provided command
        for f in self.input['flags']:
            if self.DEBUG:
                print("Validating flag '" + str(f['flag']) + "'")

            if self.cliDoesFlagExist(self.input['command'], str(f['flag'])):
                if self.DEBUG:
                    print("Flag " + str(f['flag']) + " is valid")
            else:
                self.showErr("'" + f['flag'] + "' is not a valid flag for this command")

        # Ensure all required flags have been set
        flagsForCurrentCommand = self.cliGetActionConfigByName(self.input['command'])['flags']
        flagsInInput = [o['flag'] for o in self.input['flags']]

        # Loop through all possible flags for the command
        for f in flagsForCurrentCommand:
            # Only check the required ones
            if f['isRequired']:
                # Check if the flag is in the input
                if "-" + f['shortForm'] in flagsInInput or "--" + f['longForm'] in flagsInInput:
                    if self.DEBUG:
                        print("Required flag '" + str(f['shortForm']) + "' was found")
                else:
                    self.showErr("The flag '--" + f['longForm'] + " | -" + f['shortForm'] + "' is a required option. Please add the flag before continuing.")

        # TODO - add validation with flag['val'] = required/optional/null.


    def cliShowHelp(self):
        """Show the help page, autogenerated based on settings
        """
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
                if not f['isRequired']:
                    s += " (optional)"

                s += self.nl

            if len(a['flags']) > 0:
                s += self.nl
        # Output the help string
        print(s)


    def cliDoesActionExist(self, actionName):
        """Checks if the action exists
        """
        return not self.cliGetActionConfigByName(actionName) == None


    def cliDoesFlagExist(self, actionName, flagName):
        """Checks if the action exists
        """
        return not self.cliGetFlagInfo(actionName, flagName) == None

    def cliGetActionConfigByName(self, actionName):
        """Returns the full configuration by the action name
        """

        for x in self.config['actions']:
            if x['name'] == actionName:
                if self.DEBUG:
                    print("i found it! " + x['description'])
                return x

        return None

    def cliGetFlagInfo(self, action, flagstr):
        """Gets flag configuration info by flag name

        """

        # First, get the action configuration info, which contains the flags
        actionConfig = self.cliGetActionConfigByName(action)

        if actionConfig == None:
            return None


        for x in actionConfig['flags']:

            if "-" + x['shortForm'] == flagstr:
                if self.DEBUG:
                    print("i found the flag (short)! " + x['description'])
                return x
            elif "--" + x['longForm'] == flagstr:
                if self.DEBUG:
                    print("i found the flag (long)! " + x['description'])
                return x

        return None

    def cliHandler(self):
        """Initial entrypoint for CLI usage

        """

        # Display help info if no params are provided
        if self.input['command'] == None:
            return self.cliShowHelp()

        # Get the config info for the provided action
        else:
            actionConfig = self.cliGetActionConfigByName(self.input['command'])
            if actionConfig is None:
                return self.showErr("The command '" + self.input['command'] +
                                    "' is not a valid command")

        # Run the handler for the provided action
        getattr(self, actionConfig['handlerFunction'])(actionConfig, self.input['flags'])

    def showErr(self, msg):
        """Display an error, exit with exit code 1
        """

        print("ERROR: " + msg + self.nl)
        # print("Run '" + self.config['programInfo']['name'] + " --help' for more info" + self.nl)
        print("Run '" + self.config['programInfo']['name'] +
              "' with no arguments for more info" + self.nl)
        exit(1)

    """
    DON'T EDIT FUNCTIONS ABOVE HERE - these are the CLI famework

    Below here is where all the custom functions are placed, such as handlers
    and helpers.

    """
    def fail(self, msg):
        print("Action failed: " + msg + self.nl)
        print("Please correct the error and try again." + self.nl)
        exit(1)

    def featureBranchHandler(self, options, flags):

        # Update settings here
        charLimit=30
        requiredBaseBranch="develop"

        # Parse out fields from CLI input - initialize them first
        ticketNum = ''
        feature = ''
        verbose = False

        # Loop through inputs to grab the data we want
        for f in flags:
            if f['flag'] == "-t" or f['flag'] == "--ticket":
                ticketNum = f['value'].lower()

            if (f['flag'] == "-f" or f['flag'] == "--feature") and not f['value'] == None:
                feature = f['value'].lower().replace(" ", "-")

            if f['flag'] == "-v" or f['flag'] == "--verbose":
                verbose = True

        # Check length
        if len(feature) > charLimit:
            self.fail("Feature string is " + str(len(feature) - charLimit) + " characters too long. Please shorten.")

        branchName = "feature/" + ticketNum + "-" + feature
        if self.DEBUG:
            print("Branch name found: " + branchName)

        # Check if on the right branch
        gitBranch = os.popen("git rev-parse --abbrev-ref HEAD").read().rstrip()

        if verbose:
            print("Currently on " + gitBranch)

        if requiredBaseBranch != gitBranch:
            self.fail("You must start by basing your new branch off '" + requiredBaseBranch + "'. You are currently on '" + gitBranch + "'. Please switch branches and try again.")

        # Check if git directory is clean
        gitStatus = os.popen("git status --porcelain").read()


        if len(gitStatus) > 0:
            self.fail("Can not make branch with dirty working directory. Please look at 'git status' for uncommitted files and clean up before trying again.")


        # If made to here, checks passed. Make the branch.
        print("Making new feature branch at '" + branchName + "'.")
        os.popen("git checkout -b " + branchName).read()


# Init handler
if __name__ == '__main__':
    """Init handler
    """

    githelp = GitHelp(sys.argv)
