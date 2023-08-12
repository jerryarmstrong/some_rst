tests/ui/closures/print/closure-print-generic-verbose-1.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zverbose

fn to_fn_once<F:FnOnce()>(f: F) -> F { f }

fn f<T: std::fmt::Display>(y: T) {
    struct Foo<U: std::fmt::Display> {
        x: U
    };

    let foo =  Foo{ x: "x" };

    let c = to_fn_once(move|| {
        println!("{} {}", foo.x, y);
    });

    c();
    c();
    //~^ ERROR use of moved value
}


fn main() {
    f("S");
}


