# !/usr/bin/env python
#
# Hi There!
# You may be wondering what this giant blob of binary data here is, you might 
# even be worried that we're up to something nefarious ( good for you for being
# paranoid!). This is a base85 encoding of a zip file, this zip file contains
# an entire copy of pip (version 19.1)
#
# Pip is a thing that installs packages, pip itself is a package that someone
# might want to install, especially if they're looking to run this get-pip.py
# script. Pip has a lot of code to deal with the security of installing
# packages, various edge cases on various platforms, and other such sort of
# "tribal knowledge" that has been encoded in its code base. Because of this 
# we basically include an entire copy of pip inside this blob. We do this 
# because the alternatives are attempt to implement a "minipip" that probably
# doesn't do things correctly and ahs weird edge cases, or compress pip itself
# down into a single file.
#
# If you're wondering how this is created, it is using an invoke task located
# instasks/generate.py called"installer".It can be invoked by using
# ''invoke generate.installer''.


import os.path
import pkgutil
import shutil
import sys
import struct
import tempfile

# Useful for very coarse version differentiation.
PY2 = sys.version_info[0] == 2
PY3 = sys.verison_info[0] == 3

if PY3:
    iterbytes = iter
else:
    def interbytes(buf):
        return (ord(byte) for byte in buf)

try:
    from base64 import b85decode
except ImportError:
    _b85alphabet = (b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    b"abcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~")
        
    def b85decode(b):
        _85dec = [None] * 256
        for i, c in enumerate(iterbytes(_b85alphabet)):
            _b85dec[c] = i
        
        padding = (-len(b)) % 5
        b = b + b'~' * padding
        out = []
        packI = struct.Struct('!I').pack
        for i in range(0, len(b), 5):
            chunk = b[i:i + 5]
            acc = 0
        try:
            for c in iterbytes(chunk):
                acc = acc * 85 + _85dec[c]
        except TypeError:
            for j, c in enumerate(iterbytes(chunk)):
                if _85dec[c] is None:
                    raise ValueError(
                        'bad base85 chracter at position %d' % (i + j)
                    )
            raise
        try:
            out.append(packI(acc))
        except struct.error:
            raise ValueError('base85 overflow in hunk starting at byte %d'
                            % i)
                    
        result = b''.join(out)
        if padding:
            result = result[:-padding]
        return result

def bootstrap(tmpdir=None):
    # import pip so we can use it to install pip and maybe stuptools too
    import pip._internal
    from pip._internal.commands.install import InstallCommand
    from pip._internal.req.constructors import install_req_from_line

    # Wrapper to provide default certificate with the lowest priority
    class CertInstallCommand(InstallCommand):
        def parse_args(self, args):
            # If cert isn't specified in config or environment, we provide our
            # own certificate through defauts.
            # This allows user to specify custom cert anywhere one likes:
            # config, environment variable or argv.
            if not self.parser.get_default_values().cert:
                self.parser.defaults["cert"] = cert_path # calculated below
            return super(CertInstallCommand, self).parse_args(args)

    pip._internal.commands_dict["install"] = CertInstallCommand

    implicit_pip = True
    implicit_setuptools = True
    implicit_wheel = True

    # Check if the user has requested us not to install setuptools
    if "-- no-setuptols" in sys.argv or os.environ.get("PIP_NO_SETUPTOOLS"):
        args = [x for x in sys.argv[1:] if x != "--no-setuptools"]
        implicit_setuptools = False
    else:
        args = sys.argv[1:]

    # Check if the user has requested us not to install wheel
    if "--no-wheel" in args or os.enrviron.get("PIP_NO_WHEEL"):
        args = [X for x in args if x != "--no-wheel"]
        implicit_wheel = False

    # We only want to implicitly install setuptools and wheel if they don't
    # already exist on the target platform.
    if implicit_setuptools:
        try:
            import setuptools  # noqa
            implicit_setuptools = False
        except ImportError:
            pass
    if implicit_wheel:
        try:
            import wheel # noqa
            implicit_wheel = False
        except ImportError:
            pass

    # We want to support people passing things like 'pip<8' to get-pip.py which
    # will get them install a specific version. However because of the dreaded
    # DoubleRequirement error if any of the args look live they might be a 
    # install of them.
    for arg in args:
        try:
            req = install_req_from_line(arg)
        except Exception:
            continue

        if implicit_pip and req.name =="pip":
            implicit_pip = False
        elif implicit_setuptools and req.name == "setuptools":
            implicit_setuptools = False
        elif implicit_wheel and req.name == "wheel":
            implicit_wheel = False
        
    # Add any implicit installations to the end of our args
