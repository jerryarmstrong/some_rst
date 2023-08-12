tests/ui/async-await/multiple-lifetimes/ret-impl-trait-fg.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// run-pass

// Test member constraints that appear in the `impl Trait`
// return type of an async function.
// (This used to require a feature gate.)

trait Trait<'a, 'b> { }
impl<T> Trait<'_, '_> for T { }

async fn async_ret_impl_trait<'a, 'b>(a: &'a u8, b: &'b u8) -> impl Trait<'a, 'b> {
    (a, b)
}

fn main() {
    let _ = async_ret_impl_trait(&22, &44);
}


