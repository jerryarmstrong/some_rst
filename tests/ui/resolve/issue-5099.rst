tests/ui/resolve/issue-5099.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait B <A> {
    fn a() -> A {
        this.a //~ ERROR cannot find value `this` in this scope
    }
    fn b(x: i32) {
        this.b(x); //~ ERROR cannot find value `this` in this scope
    }
    fn c() {
        let _ = || this.a; //~ ERROR cannot find value `this` in this scope
    }
}

fn main() {}


