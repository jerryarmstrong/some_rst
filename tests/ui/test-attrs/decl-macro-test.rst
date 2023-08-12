tests/ui/test-attrs/decl-macro-test.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that declarative macros can declare tests

// check-pass
// compile-flags: --test

#![feature(decl_macro)]

macro create_test() {
    #[test]
    fn test() {}
}

macro create_module_test() {
    mod x {
        #[test]
        fn test() {}
    }
}

create_test!();
create_test!();
create_module_test!();


