tests/ui/inc-range-pat.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test old and new syntax for inclusive range patterns.

#![allow(ellipsis_inclusive_range_patterns)]

fn main() {
    assert!(match 42 { 0 ... 100 => true, _ => false });
    assert!(match 42 { 0 ..= 100 => true, _ => false });

    assert!(match 'x' { 'a' ... 'z' => true, _ => false });
    assert!(match 'x' { 'a' ..= 'z' => true, _ => false });
}


