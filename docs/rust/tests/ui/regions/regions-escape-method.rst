tests/ui/regions/regions-escape-method.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test a method call where the parameter `B` would (illegally) be
// inferred to a region bound in the method argument. If this program
// were accepted, then the closure passed to `s.f` could escape its
// argument.

struct S;

impl S {
    fn f<B, F>(&self, _: F) where F: FnOnce(&i32) -> B {
    }
}

fn main() {
    let s = S;
    s.f(|p| p) //~ ERROR lifetime may not live long enough
}


