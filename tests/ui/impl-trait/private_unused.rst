tests/ui/impl-trait/private_unused.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

#[deny(warnings)]

enum Empty { }
trait Bar<T> {}
impl Bar<Empty> for () {}

fn boo() -> impl Bar<Empty> {}

fn main() {
    boo();
}


