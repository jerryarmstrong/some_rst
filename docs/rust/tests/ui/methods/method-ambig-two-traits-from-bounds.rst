tests/ui/methods/method-ambig-two-traits-from-bounds.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait A { fn foo(&self); }
trait B { fn foo(&self); }

fn foo<T:A + B>(t: T) {
    t.foo(); //~ ERROR E0034
}

fn main() {}


