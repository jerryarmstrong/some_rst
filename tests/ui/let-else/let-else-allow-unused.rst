tests/ui/let-else/let-else-allow-unused.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // issue #89807



#[deny(unused_variables)]

fn main() {
    let value = Some(String::new());
    #[allow(unused)]
    let banana = 1;
    #[allow(unused)]
    let Some(chaenomeles) = value.clone() else { return }; // OK

    let Some(chaenomeles) = value else { return }; //~ ERROR unused variable: `chaenomeles`
}


