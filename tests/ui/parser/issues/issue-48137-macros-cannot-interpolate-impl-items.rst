tests/ui/parser/issues/issue-48137-macros-cannot-interpolate-impl-items.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {}

macro_rules! mac_impl {
    ($i:item) => {
        struct S;
        impl S { $i }
    }
}

mac_impl! {
    fn foo() {}
}

macro_rules! mac_trait {
    ($i:item) => {
        trait T { $i }
    }
}

mac_trait! {
    fn foo() {}
}

macro_rules! mac_extern {
    ($i:item) => {
        extern "C" { $i }
    }
}

mac_extern! {
    fn foo();
}


