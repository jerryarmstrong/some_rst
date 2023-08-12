tests/rustdoc-ui/macro-docs.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

macro_rules! m {
    () => {
        /// A
        //~^ WARNING
        #[path = "auxiliary/module_macro_doc.rs"]
        pub mod mymodule;
    }
}

m!();


