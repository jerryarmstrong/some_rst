tests/ui/borrowck/borrowck-issue-2657-2.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
fn main() {

    let x: Option<Box<_>> = Some(Box::new(1));

    match x {
      Some(ref y) => {
        let _b = *y; //~ ERROR cannot move out
      }
      _ => {}
    }
}


