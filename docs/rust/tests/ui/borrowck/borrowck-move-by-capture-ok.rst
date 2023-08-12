tests/ui/borrowck/borrowck-move-by-capture-ok.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

pub fn main() {
    let bar: Box<_> = Box::new(3);
    let h = || -> isize { *bar };
    assert_eq!(h(), 3);
}


