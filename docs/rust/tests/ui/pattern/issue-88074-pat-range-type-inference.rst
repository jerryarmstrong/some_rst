tests/ui/pattern/issue-88074-pat-range-type-inference.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

trait Zero {
    const ZERO: Self;
}

impl Zero for i32 {
    const ZERO: Self = 0;
}

fn main() {
    match 1 {
        Zero::ZERO ..= 1 => {},
        _ => {},
    }
}


