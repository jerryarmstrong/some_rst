tests/ui/rfc-2632-const-trait-impl/static-const-trait-bound.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
pub struct S<T, F: FnOnce() -> T = fn() -> T> {
    f: F,
    x: Option<T>,
}

impl<T, F: FnOnce() -> T> S<T, F> {
    pub const fn new(f: F) -> Self {
        Self { f, x: None }
    }
}

#[derive(Default)]
pub struct Foo;

static LOCKED_CALLSITES: S<Foo> = S::new(Default::default);

fn main() {}


