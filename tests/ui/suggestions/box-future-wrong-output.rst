tests/ui/suggestions/box-future-wrong-output.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Issue #72117
// edition:2018

use core::future::Future;
use core::pin::Pin;

pub type BoxFuture<'a, T> = Pin<Box<dyn Future<Output = T> + Send + 'a>>;

impl<T: ?Sized> FutureExt for T where T: Future {}
trait FutureExt: Future {
    fn boxed<'a>(self) -> BoxFuture<'a, Self::Output>
    where
        Self: Sized + Send + 'a,
    {
        Box::pin(self)
    }
}

fn main() {
    let _: BoxFuture<'static, bool> = async {}.boxed();
    //~^ ERROR: mismatched types
}


