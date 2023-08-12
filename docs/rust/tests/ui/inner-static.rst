tests/ui/inner-static.rs
========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:inner_static.rs


extern crate inner_static;

pub fn main() {
    let a = inner_static::A::<()> { v: () };
    let b = inner_static::B::<()> { v: () };
    let c = inner_static::test::A::<()> { v: () };
    assert_eq!(a.bar(), 2);
    assert_eq!(b.bar(), 4);
    assert_eq!(c.bar(), 6);
}


