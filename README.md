# githelp.py
## a git helper in python

Goals: provide developers new to the terminal assistance in using a good workflow. For example - creating feature branches based on ticket numbers.

How-to is provided at runtime:

```
githelp.py v0.0.2
Git CLI helper for developers

Usage: githelp.py [command] --flag1 --flag2 --flag3=val

Commands available:

   newfeature : Create a new feature branch, with some safety checks
       -t <tknum>  [OR] --ticket=<tknum>	  Ticket number
       -f <featname>  [OR] --feature=<featname>	  Short feature description
       -v [OR] --verbose	  Make output verbose (optional)

       Example usage of command [newfeature] : 
          githelp.py newfeature -t ba-123 -f bootstrap-upgrade
          githelp.py newfeature --ticket=ba-123 --feature=bootstrap-upgrade

```

More features to be possibly added in the future.

Also - no external library use, using only the built-in python modules.


