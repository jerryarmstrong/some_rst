tests/ui/array-slice-vec/ivec-pass-by-value.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn f(_a: Vec<isize> ) { }
pub fn main() { f(vec![1, 2, 3, 4, 5]); }


