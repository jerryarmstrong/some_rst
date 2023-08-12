tests/ui/parser/raw/raw-literal-self.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let r#self: ();
    //~^ ERROR `self` cannot be a raw identifier
}


