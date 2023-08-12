tests/ui/issues/issue-5988.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

trait B {
    fn f(&self);
}

trait T : B {
}

struct A;

impl<U: T> B for U {
    fn f(&self) { }
}

impl T for A {
}

fn main() {
    let a = A;
    let br = &a as &dyn B;
    br.f();
}


