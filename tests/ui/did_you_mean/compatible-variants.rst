tests/ui/did_you_mean/compatible-variants.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Hey<A, B> {
    A(A),
    B(B),
}

struct Foo {
    bar: Option<i32>,
}

fn f() {}

fn a() -> Option<()> {
    while false {
        //~^ ERROR mismatched types
        f();
    }
    //~^ HELP try adding an expression
}

fn b() -> Result<(), ()> {
    f()
    //~^ ERROR mismatched types
    //~| HELP try adding an expression
}

fn c() -> Option<()> {
    for _ in [1, 2] {
        //~^ ERROR mismatched types
        f();
    }
    //~^ HELP try adding an expression
}

fn d() -> Option<()> {
    c()?
    //~^ ERROR incompatible types
    //~| HELP try removing this `?`
    //~| HELP try adding an expression
}

fn main() {
    let _: Option<()> = while false {};
    //~^ ERROR mismatched types
    //~| HELP try wrapping
    let _: Option<()> = {
        while false {}
        //~^ ERROR mismatched types
        //~| HELP try adding an expression
    };
    let _: Result<i32, i32> = 1;
    //~^ ERROR mismatched types
    //~| HELP try wrapping
    let _: Option<i32> = 1;
    //~^ ERROR mismatched types
    //~| HELP try wrapping
    let _: Hey<i32, i32> = 1;
    //~^ ERROR mismatched types
    //~| HELP try wrapping
    let _: Hey<i32, bool> = false;
    //~^ ERROR mismatched types
    //~| HELP try wrapping
    let bar = 1i32;
    let _ = Foo { bar };
    //~^ ERROR mismatched types
    //~| HELP try wrapping
}

enum A {
    B { b: B },
}

struct A2(B);

enum B {
    Fst,
    Snd,
}

fn foo() {
    let a: A = B::Fst;
    //~^ ERROR mismatched types
    //~| HELP try wrapping
}

fn bar() {
    let a: A2 = B::Fst;
    //~^ ERROR mismatched types
    //~| HELP try wrapping
}


