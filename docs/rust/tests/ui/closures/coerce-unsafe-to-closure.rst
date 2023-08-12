tests/ui/closures/coerce-unsafe-to-closure.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x: Option<&[u8]> = Some("foo").map(std::mem::transmute);
    //~^ ERROR E0277
}


