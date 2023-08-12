tests/ui/suggestions/issue-106443-sugg-clone-for-arg.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Clone)]
struct S;

// without Clone
struct T;

fn foo(_: S) {}

fn test1() {
    let s = &S;
    foo(s); //~ ERROR mismatched types
}

fn bar(_: T) {}
fn test2() {
    let t = &T;
    bar(t); //~ ERROR mismatched types
}

fn main() {
    test1();
    test2();
}


