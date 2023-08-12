tests/ui/str/str-array-assignment.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
  let s = "abc";
  let t = if true { s[..2] } else { s };
  //~^ ERROR `if` and `else` have incompatible types
  let u: &str = if true { s[..2] } else { s };
  //~^ ERROR mismatched types
  let v = s[..2];
  //~^ ERROR the size for values of type
  let w: &str = s[..2];
  //~^ ERROR mismatched types
}


