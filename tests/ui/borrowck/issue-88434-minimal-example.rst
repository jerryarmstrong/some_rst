tests/ui/borrowck/issue-88434-minimal-example.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test related to issue 88434

const _CONST: &() = &f(&|_| {});
//~^ constant

const fn f<F>(_: &F)
where
    F: FnMut(&u8),
{
    panic!() //~ ERROR evaluation of constant value failed
    //~^ panic
}

fn main() { }


