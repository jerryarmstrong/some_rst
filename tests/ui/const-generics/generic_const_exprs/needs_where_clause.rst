tests/ui/const-generics/generic_const_exprs/needs_where_clause.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]
#![feature(generic_const_exprs)]
#![allow(incomplete_features)]

const fn complex_maths<T>(n : usize) -> usize {
  2 * n + 1
}

struct Example<T, const N: usize> {
  a: [f32; N],
  b: [f32; complex_maths::<T>(N)],
  //~^ ERROR unconstrained
  c: T,
}


