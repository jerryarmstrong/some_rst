tests/ui/overloaded/overloaded-calls-object-two-args.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Tests calls to closure arguments where the closure takes 2 arguments.
// This is a bit tricky due to rust-call ABI.


fn foo(f: &mut dyn FnMut(isize, isize) -> isize) -> isize {
    f(1, 2)
}

fn main() {
    let z = foo(&mut |x, y| x * 10 + y);
    assert_eq!(z, 12);
}


