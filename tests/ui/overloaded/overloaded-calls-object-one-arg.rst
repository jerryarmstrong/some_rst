tests/ui/overloaded/overloaded-calls-object-one-arg.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Tests calls to closure arguments where the closure takes 1 argument.
// This is a bit tricky due to rust-call ABI.


fn foo(f: &mut dyn FnMut(isize) -> isize) -> isize {
    f(22)
}

fn main() {
    let z = foo(&mut |x| x *100);
    assert_eq!(z, 2200);
}


