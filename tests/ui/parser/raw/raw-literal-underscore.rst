tests/ui/parser/raw/raw-literal-underscore.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let r#_: ();
    //~^ ERROR `_` cannot be a raw identifier
}


