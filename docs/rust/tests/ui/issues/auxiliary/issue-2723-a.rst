tests/ui/issues/auxiliary/issue-2723-a.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub unsafe fn f(xs: Vec<isize> ) {
    xs.iter().map(|_x| { unsafe fn q() { panic!(); } }).collect::<Vec<()>>();
}


