tests/ui/overloaded/overloaded-calls-object-zero-args.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Tests calls to closure arguments where the closure takes 0 arguments.
// This is a bit tricky due to rust-call ABI.


fn foo(f: &mut dyn FnMut() -> isize) -> isize {
    f()
}

fn main() {
    let z = foo(&mut || 22);
    assert_eq!(z, 22);
}


