tests/ui/never_type/auto-traits.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(auto_traits)]
#![feature(negative_impls)]
#![feature(never_type)]

fn main() {
    enum Void {}

    auto trait Auto {}
    fn assert_auto<T: Auto>() {}
    assert_auto::<Void>();
    assert_auto::<!>();

    fn assert_send<T: Send>() {}
    assert_send::<Void>();
    assert_send::<!>();
}


