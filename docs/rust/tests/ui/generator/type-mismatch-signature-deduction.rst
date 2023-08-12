tests/ui/generator/type-mismatch-signature-deduction.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generators, generator_trait)]

use std::ops::Generator;

fn foo() -> impl Generator<Return = i32> {
    //~^ ERROR type mismatch
    || {
        if false {
            return Ok(6);
        }

        yield ();

        5 //~ ERROR mismatched types [E0308]
    }
}

fn main() {}


