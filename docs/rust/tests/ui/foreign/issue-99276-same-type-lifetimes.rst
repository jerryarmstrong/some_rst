tests/ui/foreign/issue-99276-same-type-lifetimes.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we do not ICE when structurally comparing types with lifetimes present.
// check-pass

pub struct Record<'a> {
    pub args: &'a [(usize, &'a str)],
}

mod a {
    extern "Rust" {
        fn foo<'a, 'b>(record: &'a super::Record<'b>);

        fn bar<'a, 'b>(record: &'a super::Record<'b>);
    }
}

mod b {
    extern "Rust" {
        fn foo<'a, 'b>(record: &'a super::Record<'b>);

        fn bar<'a, 'b>(record: &'a super::Record<'b>);
    }
}

fn main() {}


