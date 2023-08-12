tests/ui/sized/recursive-type-1.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
trait A { type Assoc; }

impl A for () {
    // FIXME: it would be nice for this to at least cause a warning.
    type Assoc = Foo<()>;
}
struct Foo<T: A>(T::Assoc);

fn main() {}


