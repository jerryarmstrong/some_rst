tests/ui/rust-2018/uniform-paths/fn-local-enum.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
// edition:2018

fn main() {
    enum E { A, B, C }

    use E::*;
    match A {
        A => {}
        B => {}
        C => {}
    }
}


