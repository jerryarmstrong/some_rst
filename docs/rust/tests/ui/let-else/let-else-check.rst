tests/ui/let-else/let-else-check.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unused_variables)]

fn main() {
    // type annotation, attributes
    #[allow(unused_variables)]
    let Some(_): Option<u32> = Some(Default::default()) else {
        let x = 1; // OK
        return;
    };

    let Some(_): Option<u32> = Some(Default::default()) else {
        let x = 1; //~ ERROR unused variable: `x`
        return;
    };

    let x = 1; //~ ERROR unused variable: `x`
}


