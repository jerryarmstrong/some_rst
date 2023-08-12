tests/ui/consts/std/iter.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

const I: std::iter::Empty<u32> = std::iter::empty();

fn main() {
    for i in I {
        panic!("magical value creation: {}", i);
    }
}


