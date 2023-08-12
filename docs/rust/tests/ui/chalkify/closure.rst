tests/ui/chalkify/closure.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z trait-solver=chalk

fn main() -> () {
    let t = || {};
    t();

    let mut a = 0;
    let mut b = move || {
        a = 1;
    };
    b();

    let mut c = b;

    c();
    b();

    let mut a = 0;
    let mut b = || {
        a = 1;
    };
    b();

    let mut c = b;

    c();
    b(); //~ ERROR

    // FIXME(chalk): this doesn't quite work
    /*
    let b = |c| {
        c
    };

    let a = &32;
    b(a);
    */
}


