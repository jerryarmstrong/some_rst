tests/rustdoc/auxiliary/pub-use-extern-macros.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name="macros"]

#[macro_export]
macro_rules! foo {
    () => {};
}

#[macro_export]
macro_rules! bar {
    () => {};
}

#[macro_export]
macro_rules! baz {
    () => {};
}

#[macro_export]
macro_rules! quux {
    () => {};
}


