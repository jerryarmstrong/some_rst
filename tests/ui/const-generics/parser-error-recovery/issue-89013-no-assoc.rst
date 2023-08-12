tests/ui/const-generics/parser-error-recovery/issue-89013-no-assoc.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo<const N: usize> {
    fn do_x(&self) -> [u8; N];
}

struct Bar;

const T: usize = 42;

impl Foo<const 3> for Bar {
//~^ERROR expected lifetime, type, or constant, found keyword `const`
    fn do_x(&self) -> [u8; 3] {
        [0u8; 3]
    }
}

fn main() {}


