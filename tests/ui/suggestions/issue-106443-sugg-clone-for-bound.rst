tests/ui/suggestions/issue-106443-sugg-clone-for-bound.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Clone)]
struct S;

trait X {}

impl X for S {}

fn foo<T: X>(_: T) {}
fn bar<T: X>(s: &T) {
    foo(s); //~ ERROR the trait bound `&T: X` is not satisfied
}

fn bar_with_clone<T: X + Clone>(s: &T) {
    foo(s); //~ ERROR the trait bound `&T: X` is not satisfied
}

fn main() {
    let s = &S;
    bar(s);
}


