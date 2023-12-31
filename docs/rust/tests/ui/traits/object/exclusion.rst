tests/ui/traits/object/exclusion.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
trait Future: 'static {
    // The requirement for Self: Sized must prevent instantiation of
    // Future::forget in vtables, otherwise there's an infinite type
    // recursion through <Map<...> as Future>::forget.
    fn forget(self) where Self: Sized {
        Box::new(Map(self)) as Box<dyn Future>;
    }
}

struct Map<A>(#[allow(unused_tuple_struct_fields)] A);
impl<A: Future> Future for Map<A> {}

pub struct Promise;
impl Future for Promise {}

fn main() {
    Promise.forget();
}


