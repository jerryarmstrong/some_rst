tests/ui/methods/method-ambig-two-traits-from-impls2.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait A { fn foo(); }
trait B { fn foo(); }

struct AB {}

impl A for AB {
    fn foo() {}
}

impl B for AB {
    fn foo() {}
}

fn main() {
    AB::foo();  //~ ERROR E0034
}


