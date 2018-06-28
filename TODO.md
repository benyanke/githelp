# Todo

## Goal

Keep everything in a single file, so there is easy deployment
to remote systems by copying a single file.


## Functions / Sections Needed

### CLI Framework

Single variable containing an array of arrays with the CLI signagure of all the options. In the top level, 
a listing of actions, with the following properties:

  - action cli name (newfeature)
  - description (eg: make new feature branch)
  - handler function (this function is passed the flags when the action is called)
  
And under each action, an arrya of possible flags. Each flag has the following properties:

  - short form (-v)
  - long form (--verbose)
  - description (for help)
  - isRequired (bool)
  - val (set to 'required' | 'optional' | None)
  - valName (name of the paramater, if exists - set to None for flags not accepting a paramater)

And finally, a set of global flags, using the same params as above, except without the required option.


### Git functions

**Low Level git-call functions**

  - git status
  - git getCurrentBranch (reads the current branch state)
  - git makeNewBranch (makes a new branch)

  TODO: add some functions around detatched heads here as wello


**Higher level functions**

  - git isWorkDirClean



