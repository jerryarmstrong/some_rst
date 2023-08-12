tests/ui/sized-cycle-note.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Baz { q: Option<Foo> }
//~^ ERROR recursive types `Baz` and `Foo` have infinite size
struct Foo { q: Option<Baz> }

impl Foo { fn bar(&self) {} }

fn main() {}


