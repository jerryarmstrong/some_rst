tests/ui/rfc-2091-track-caller/pass.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// revisions: default mir-opt
//[mir-opt] compile-flags: -Zmir-opt-level=4

#[track_caller]
fn f() {}

fn main() {
    f();
}


