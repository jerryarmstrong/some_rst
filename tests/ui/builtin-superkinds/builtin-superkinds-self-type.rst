tests/ui/builtin-superkinds/builtin-superkinds-self-type.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests (negatively) the ability for the Self type in default methods
// to use capabilities granted by builtin kinds as supertraits.

use std::sync::mpsc::{channel, Sender};

trait Foo : Sized+Sync+'static {
    fn foo(self, mut chan: Sender<Self>) { }
}

impl <T: Sync> Foo for T { }
//~^ ERROR the parameter type `T` may not live long enough

fn main() {
    let (tx, rx) = channel();
    1193182.foo(tx);
    assert_eq!(rx.recv(), 1193182);
}


