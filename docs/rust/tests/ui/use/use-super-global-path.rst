tests/ui/use/use-super-global-path.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused)]

struct S;
struct Z;

mod foo {
    use ::super::{S, Z}; //~ ERROR global paths cannot start with `super`
                         //~| ERROR global paths cannot start with `super`

    pub fn g() {
        use ::super::main; //~ ERROR global paths cannot start with `super`
        main();
    }
}

fn main() { foo::g(); }


