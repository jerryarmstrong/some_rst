tests/ui/destructuring-assignment/slice_destructure_fail.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
  let (mut a, mut b);
  [a, .., b, ..] = [0, 1]; //~ ERROR `..` can only be used once per slice pattern
  [a, a, b] = [1, 2]; //~ ERROR pattern requires 3 elements but array has 2
  [_] = [1, 2]; //~ ERROR pattern requires 1 element but array has 2
}


