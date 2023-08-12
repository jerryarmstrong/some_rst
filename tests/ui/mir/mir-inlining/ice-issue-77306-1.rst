tests/ui/mir/mir-inlining/ice-issue-77306-1.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags:-Zmir-opt-level=3

// Previously ICEd because we did not normalize during inlining,
// see https://github.com/rust-lang/rust/pull/77306 for more discussion.

pub fn write() {
    create()()
}

pub fn create() -> impl FnOnce() {
   || ()
}

fn main() {
    write();
}


