tests/ui/expr-block-fn.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn test_fn() {
    fn ten() -> isize { return 10; }
    let rs = ten;
    assert_eq!(rs(), 10);
}

pub fn main() { test_fn(); }


