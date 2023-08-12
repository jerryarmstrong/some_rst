tests/ui/parser/nested-missing-closing-angle-bracket.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
  let v : Vec::<Vec<(u32,_,_)> = vec![vec![]];
    //~^ ERROR: expected one of
}


