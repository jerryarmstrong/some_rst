tests/ui/associated-consts/defaults-cyclic-fail.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail

// Cyclic assoc. const defaults don't error unless *used*
trait Tr {
    const A: u8 = Self::B;
    //~^ cycle detected when const-evaluating + checking `Tr::A`

    const B: u8 = Self::A;
}

// This impl is *allowed* unless its assoc. consts are used
impl Tr for () {}

fn main() {
    // This triggers the cycle error
    assert_eq!(<() as Tr>::A, 0);
}


