tests/ui/resolve/issue-65035-static-with-parent-generics.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f<T>() {
    extern "C" {
        static a: *const T;
        //~^ ERROR can't use generic parameters from outer function
    }
}

fn g<T: Default>() {
    static a: *const T = Default::default();
    //~^ ERROR can't use generic parameters from outer function
}

fn h<const N: usize>() {
    extern "C" {
        static a: [u8; N];
        //~^ ERROR can't use generic parameters from outer function
    }
}

fn i<const N: usize>() {
    static a: [u8; N] = [0; N];
    //~^ ERROR can't use generic parameters from outer function
    //~| ERROR can't use generic parameters from outer function
}

fn main() {}


