tests/ui/traits/inherent-method-order.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

struct Foo;

impl Foo {
    #[allow(dead_code)]
    fn foo(self) {
        panic!("wrong method!")
    }
}

trait Trait {
    fn foo(self);
}

impl<'a,'b,'c> Trait for &'a &'b &'c Foo {
    fn foo(self) {
        // ok
    }
}

fn main() {
    let x = &(&(&Foo));
    x.foo();
}


