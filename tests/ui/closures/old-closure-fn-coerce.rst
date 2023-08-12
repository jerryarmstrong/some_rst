tests/ui/closures/old-closure-fn-coerce.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_braces)]

fn force<F>(f: F) -> isize where F: FnOnce() -> isize { return f(); }

pub fn main() {
    fn f() -> isize { return 7; }
    assert_eq!(force(f), 7);
    let g = {||force(f)};
    assert_eq!(g(), 7);
}


