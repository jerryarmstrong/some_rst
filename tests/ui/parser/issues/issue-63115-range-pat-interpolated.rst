tests/ui/parser/issues/issue-63115-range-pat-interpolated.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(exclusive_range_pattern)]

#![allow(ellipsis_inclusive_range_patterns)]

fn main() {
    macro_rules! mac_expr {
        ($e:expr) => {
            if let 2...$e = 3 {}
            if let 2..=$e = 3 {}
            if let 2..$e = 3 {}
            if let ..$e = 3 {}
            if let ..=$e = 3 {}
            if let $e.. = 5 {}
            if let $e..5 = 4 {}
            if let $e..=5 = 4 {}
        }
    }
    mac_expr!(4);
}


