src/tools/clippy/tests/ui/missing_trait_methods.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused, clippy::needless_lifetimes)]
#![warn(clippy::missing_trait_methods)]

trait A {
    fn provided() {}
}

trait B {
    fn required();

    fn a(_: usize) -> usize {
        1
    }

    fn b<'a, T: AsRef<[u8]>>(a: &'a T) -> &'a [u8] {
        a.as_ref()
    }
}

struct Partial;

impl A for Partial {}

impl B for Partial {
    fn required() {}

    fn a(_: usize) -> usize {
        2
    }
}

struct Complete;

impl A for Complete {
    fn provided() {}
}

impl B for Complete {
    fn required() {}

    fn a(_: usize) -> usize {
        2
    }

    fn b<T: AsRef<[u8]>>(a: &T) -> &[u8] {
        a.as_ref()
    }
}

fn main() {}


