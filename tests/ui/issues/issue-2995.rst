tests/ui/issues/issue-2995.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn bad (p: *const isize) {
    let _q: &isize = p as &isize; //~ ERROR non-primitive cast
}

fn main() { }


