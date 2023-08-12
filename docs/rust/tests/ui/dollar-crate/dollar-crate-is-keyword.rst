tests/ui/dollar-crate/dollar-crate-is-keyword.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! m {
    () => {
        // Avoid having more than one `$crate`-named item in the same module,
        // as even though they error, they still parse as `$crate` and conflict.
        mod foo {
            struct $crate {} //~ ERROR expected identifier, found reserved identifier `$crate`
        }

        use $crate; //~ ERROR `$crate` may not be imported
        use $crate as $crate; //~ ERROR expected identifier, found reserved identifier `$crate`
        //~^ ERROR `$crate` may not be imported
    }
}

m!();

fn main() {}


