tests/ui/suggestions/slice-issue-87994.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
  let v = vec![1i32, 2, 3];
  for _ in v[1..] {
    //~^ ERROR [i32]` is not an iterator [E0277]
    //~^^ ERROR known at compilation time
  }
  struct K {
    n: i32,
  }
  let mut v2 = vec![K { n: 1 }, K { n: 1 }, K { n: 1 }];
  for i2 in v2[1..] {
    //~^ ERROR [K]` is not an iterator [E0277]
    //~^^ ERROR known at compilation time
    i2.n = 2;
  }
}


