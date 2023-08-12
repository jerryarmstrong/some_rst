tests/ui/methods/method-ambig-two-traits-from-impls.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait A { fn foo(self); }
trait B { fn foo(self); }

struct AB {}

impl A for AB {
    fn foo(self) {}
}

impl B for AB {
    fn foo(self) {}
}

fn main() {
    AB {}.foo();  //~ ERROR E0034
}


