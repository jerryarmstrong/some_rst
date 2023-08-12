tests/ui/parser/issues/issue-7222.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616
#![allow(illegal_floating_point_literal_pattern)] // FIXME #41620

pub fn main() {
    const FOO: f64 = 10.0;

    match 0.0 {
        0.0 ..= FOO => (),
        _ => ()
    }
}


