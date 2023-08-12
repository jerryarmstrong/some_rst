src/tools/miri/tests/pass/multi_arg_closure.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(f: &mut dyn FnMut(isize, isize) -> isize) -> isize {
    f(1, 2)
}

fn main() {
    let z = foo(&mut |x, y| x * 10 + y);
    assert_eq!(z, 12);
}


