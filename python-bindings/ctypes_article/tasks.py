""" Task definitions for invoke command line utility for python bindings
    ctypes article. """
import invoke
import pathlib


@invoke.task
def clean(c):
    """ Remove any built objects """
    for pattern in ["*.o", "*.so", ]:
        c.run("rm -rf {}".format(pattern))


def print_banner(msg):
    print("==================================================")
    print("= {} ".format(msg))


@invoke.task
def build_clib(c):
    """ Build the shared library for the sample C code """
    print_banner("Building C Library")
    invoke.run("gcc -c -Wall -Werror -fpic clib1.c -I /usr/include/python3.7")
    invoke.run("gcc -shared -o libclib1.so clib1.o")
    print("* Complete")


@invoke.task(build_clib)
def test(c):
    """ Run the script to test ctypes """
    print_banner("Testing ctypes Module")
    invoke.run("python3 callclib1.py", pty=True)
