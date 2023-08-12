tests/ui/associated-types/normalization-debruijn-1.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
// edition:2018

// Regression test to ensure we handle debruijn indices correctly in projection
// normalization under binders. Found in crater run for #85499

use std::future::Future;
use std::pin::Pin;
pub enum Outcome<S, E> {
    Success((S, E)),
}
pub struct Request<'r> {
    _marker: std::marker::PhantomData<&'r ()>,
}
pub trait FromRequest<'r>: Sized {
    type Error;
    fn from_request<'life0>(
        request: &'r Request<'life0>,
    ) -> Pin<Box<dyn Future<Output = Outcome<Self, Self::Error>>>>;
}
impl<'r, T: FromRequest<'r>> FromRequest<'r> for Option<T> {
    type Error = ();
    fn from_request<'life0>(
        request: &'r Request<'life0>,
    ) -> Pin<Box<dyn Future<Output = Outcome<Self, Self::Error>>>> {
        Box::pin(async move {
            let request = request;
            match T::from_request(request).await {
                _ => todo!(),
            }
        });
        todo!()
    }
}

fn main() {}


