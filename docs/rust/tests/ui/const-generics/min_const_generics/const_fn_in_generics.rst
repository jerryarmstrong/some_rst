tests/ui/const-generics/min_const_generics/const_fn_in_generics.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

const fn identity<const T: u32>() -> u32 { T }

#[derive(Eq, PartialEq, Debug)]
pub struct ConstU32<const U: u32>;

pub fn new() -> ConstU32<{ identity::<3>() }> {
  ConstU32::<{ identity::<3>() }>
}

fn main() {
  let v = new();
  assert_eq!(v, ConstU32::<3>);
}


