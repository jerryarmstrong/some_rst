tests/ui/parser/pat-ref-enum.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn matcher(x: Option<isize>) {
    match x {
      ref Some(i) => {} //~ ERROR expected identifier, found enum pattern
      None => {}
    }
}

fn main() {}


