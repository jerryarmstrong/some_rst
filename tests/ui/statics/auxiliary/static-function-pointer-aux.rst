tests/ui/statics/auxiliary/static-function-pointer-aux.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn f(x: isize) -> isize { -x }

pub static F: fn(isize) -> isize = f;
pub static mut MutF: fn(isize) -> isize = f;


