tests/ui/macros/format-parse-errors.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let foo = "";
    let bar = "";
    format!(); //~ ERROR requires at least a format string argument
    format!(struct); //~ ERROR expected expression
    format!("s", name =); //~ ERROR expected expression
    format!(
        "s {foo} {} {}",
        foo = foo,
        bar, //~ ERROR positional arguments cannot follow named arguments
    );
    format!("s {foo}", foo = struct); //~ ERROR expected expression
    format!("s", struct); //~ ERROR expected expression

    // This error should come after parsing errors to ensure they are non-fatal.
    format!(123); //~ ERROR format argument must be a string literal
}


