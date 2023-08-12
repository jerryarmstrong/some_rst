tests/ui/parser/pat-lt-bracket-1.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
  match 42 {
    x < 7 => (),
   //~^ error: expected one of `=>`, `@`, `if`, or `|`, found `<`
    _ => ()
  }
}


