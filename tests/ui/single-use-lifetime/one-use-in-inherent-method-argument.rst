tests/ui/single-use-lifetime/one-use-in-inherent-method-argument.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(single_use_lifetimes)]
#![allow(dead_code)]
#![allow(unused_variables)]

// Test that we DO warn for a lifetime used only once in an inherent method.

struct Foo<'f> {
    data: &'f u32
}

impl<'f> Foo<'f> { //~ ERROR `'f` only used once
    //~^ HELP elide the single-use lifetime
    fn inherent_a<'a>(&self, data: &'a u32) { //~ ERROR `'a` only used once
        //~^ HELP elide the single-use lifetime
    }
}

fn main() { }


