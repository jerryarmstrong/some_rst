tests/ui/const-generics/suggest_const_for_array.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

fn example<const N: usize>() {}

fn other() {
  example::<[usize; 3]>();
  //~^ ERROR type provided when a const
  example::<[usize; 4+5]>();
  //~^ ERROR type provided when a const
}


