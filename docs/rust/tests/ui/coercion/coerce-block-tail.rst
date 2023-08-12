tests/ui/coercion/coerce-block-tail.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail
fn main() {
    let _: &str = & { String::from("hahah")};
    let _: &i32 = & { Box::new(1i32) };
    //~^ ERROR mismatched types
}


