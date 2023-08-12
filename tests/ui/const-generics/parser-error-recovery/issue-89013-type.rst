tests/ui/const-generics/parser-error-recovery/issue-89013-type.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo<const N: usize> {
    fn do_x(&self) -> [u8; N];
}

struct Bar;

const T: usize = 42;

impl Foo<N = type 3> for Bar {
//~^ERROR missing type to the right of `=`
    fn do_x(&self) -> [u8; 3] {
        [0u8; 3]
    }
}

fn main() {}


