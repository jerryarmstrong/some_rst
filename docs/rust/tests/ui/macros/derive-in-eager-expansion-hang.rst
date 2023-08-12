tests/ui/macros/derive-in-eager-expansion-hang.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for the issue #44692

macro_rules! hang { () => {
    { //~ ERROR format argument must be a string literal
        #[derive(Clone)]
        struct S;

        ""
    }
}}

fn main() {
    format_args!(hang!());
}


