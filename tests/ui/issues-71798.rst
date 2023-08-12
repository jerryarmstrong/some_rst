tests/ui/issues-71798.rs
========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn test_ref(x: &u32) -> impl std::future::Future<Output = u32> + '_ {
    //~^ ERROR `u32` is not a future
    *x
}

fn main() {
    let _ = test_ref & u; //~ ERROR cannot find value `u` in this scope
}


