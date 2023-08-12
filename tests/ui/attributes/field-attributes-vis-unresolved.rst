tests/ui/attributes/field-attributes-vis-unresolved.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Non-builtin attributes do not mess with field visibility resolution (issue #67006).

mod internal {
    struct S {
        #[rustfmt::skip]
        pub(in crate::internal) field: u8 // OK
    }

    struct Z(
        #[rustfmt::skip]
        pub(in crate::internal) u8 // OK
    );
}

struct S {
    #[rustfmt::skip]
    pub(in nonexistent) field: u8 //~ ERROR failed to resolve
}

struct Z(
    #[rustfmt::skip]
    pub(in nonexistent) u8 //~ ERROR failed to resolve
);

fn main() {}


