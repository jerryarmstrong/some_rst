tests/ui/malformed/malformed-interpolated.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]

macro_rules! check {
    ($expr: expr) => (
        #[rustc_dummy = $expr]
        use main as _;
    );
}

check!("0"); // OK
check!(0); // OK
check!(0u8); //~ ERROR suffixed literals are not allowed in attributes
check!(-0); //~ ERROR unexpected expression: `-0`
check!(0 + 0); //~ ERROR unexpected expression: `0 + 0`

fn main() {}


