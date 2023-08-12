tests/ui/point-to-type-err-cause-on-impl-trait-return-2.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn unrelated() -> Result<(), std::string::ParseError> {  // #57664
    let x = 0;

    match x {
        1 => {
            let property_value_as_string = "a".parse()?;
        }
        2 => {
            let value: &bool = unsafe { &42 };
            //~^ ERROR mismatched types
        }
    };

    Ok(())
}

fn main() {}


