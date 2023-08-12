tests/ui/never_type/impl_trait_fallback.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {}

trait T {}
impl T for () {}

fn should_ret_unit() -> impl T {
    panic!()
}


