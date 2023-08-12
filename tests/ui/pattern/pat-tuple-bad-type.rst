tests/ui/pattern/pat-tuple-bad-type.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x; //~ ERROR type annotations needed

    match x {
        (..) => {}
        _ => {}
    }

    match 0u8 {
        (..) => {} //~ ERROR mismatched types
        _ => {}
    }

    x = 10;
}


