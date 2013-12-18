==========
PwnedCheck
==========

Python package to interact with http://haveibeenpwned.com


============
Installation
============

    $ pip install PwnedCheck


=====
Usage
=====

All checks are done through the `check` method. This will check a single email address against the haveibeenpwned API
and return a list of sites that the email address has been found on.

If the email address is not found in any of the data leaks, it will return an empty list (`[]`).

If the email address is invalid (not properlly formatted), `PwnedCheck` will throw an `InvalidEmail` exception.


    import pwnedcheck

    print pwnedcheck.check("foo@bar.com")



