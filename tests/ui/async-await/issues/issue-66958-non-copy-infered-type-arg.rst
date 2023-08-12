tests/ui/async-await/issues/issue-66958-non-copy-infered-type-arg.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

struct Ia<S>(S);

impl<S> Ia<S> {
    fn partial(_: S) {}
    fn full(self) {}

    async fn crash(self) {
        Self::partial(self.0);
        Self::full(self); //~ ERROR use of partially moved value: `self`
    }
}

fn main() {}


