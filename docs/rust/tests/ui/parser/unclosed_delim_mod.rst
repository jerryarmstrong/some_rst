tests/ui/parser/unclosed_delim_mod.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

pub struct Value {}
pub fn new() -> Result<Value, ()> {
    Ok(Value {
    }
}
//~^ ERROR mismatched closing delimiter


