tests/ui/impl-trait/nested-return-type4.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition: 2021

fn test<'s: 's>(s: &'s str) -> impl std::future::Future<Output = impl Sized> {
    async move { let _s = s; }
    //~^ ERROR hidden type for `impl Future<Output = impl Sized>` captures lifetime that does not appear in bounds
}

fn main() {}


