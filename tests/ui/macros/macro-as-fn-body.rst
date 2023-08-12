tests/ui/macros/macro-as-fn-body.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //
// run-pass
//
// Description - ensure Interpolated blocks can act as valid function bodies
// Covered cases: free functions, struct methods, and default trait functions

macro_rules! def_fn {
    ($body:block) => {
        fn bar() $body
    }
}

trait Foo {
    def_fn!({ println!("foo"); });
}

struct Baz {}

impl Foo for Baz {}

struct Qux {}

impl Qux {
    def_fn!({ println!("qux"); });
}

def_fn!({ println!("quux"); });

pub fn main() {
    Baz::bar();
    Qux::bar();
    bar();
}


