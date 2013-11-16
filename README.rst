---------------------------------------------------
password - hashed passwords generation utility
---------------------------------------------------

The password module offers you a single utility class called ``Password``.
This class is meant to be used as an attribute of any other object class on
which you want to store passwords in hashed mode. This module is
framework-agnostic so it is up to you to provide persistence (you need to store
'hash' and 'salt' set on the object).

Example usage
-----------------------------------------

Create your class::

    >>> import password
    >>> class User():
    ...     password = password.Password(method='sha1', hash_encoding='base64')
            # You also probably want to create 'hash' and 'salt' attributes
            # With your chosen persistence mechanism

Set a password on the object::

    >>> user = User()
    >>> user.password = 'abcdef'

You cannot read the password back::

    >>> user.password
    <password._HashedPassword object at 0x7fdba1fef990>

but you can see, that hash and salt are
set::

    >>> user.hash
    'L1Fz6aoIdIlZzoxsXPWxJq8zNTQ='
    >>> user.salt
    'VIboVvtr'

You can also check for equality with a string::

    >>> user.password == 'abcdef'
    True
    >>> user.password == '12345'
    False

