tests/ui/proc-macro/auxiliary/span-test-macros.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_export]
macro_rules! reemit_legacy {
    ($($tok:tt)*) => ($($tok)*)
}

#[macro_export]
macro_rules! say_hello_extern {
    ($macname:ident) => ( $macname! { "Hello, world!" })
}


