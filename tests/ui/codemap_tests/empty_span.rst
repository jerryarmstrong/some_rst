tests/ui/codemap_tests/empty_span.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(negative_impls)]
fn main() {
    struct Foo;

    impl !Sync for Foo {}

    unsafe impl Send for &'static Foo { } //~ ERROR cross-crate traits with a default impl
}


