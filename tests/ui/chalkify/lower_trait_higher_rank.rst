tests/ui/chalkify/lower_trait_higher_rank.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Z trait-solver=chalk

trait Foo<F: ?Sized> where for<'a> F: Fn(&'a (u8, u16)) -> &'a u8
{
}

fn main() {
}


