tests/ui/try-trait/try-on-option.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

fn foo() -> Result<u32, ()> {
    let x: Option<u32> = None;
    x?; //~ ERROR the `?` operator
    Ok(22)
}

fn bar() -> u32 {
    let x: Option<u32> = None;
    x?; //~ ERROR the `?` operator
    22
}


