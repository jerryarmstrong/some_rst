tests/ui/rfc-2632-const-trait-impl/const-impl-norecover.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_trait_impl)]

struct Foo;

const impl Foo { //~ ERROR: expected identifier, found keyword
    fn bar() {}
}

fn main() {
     // shouldn't error here because we shouldn't have been able to recover above
     Foo::bar();
}


