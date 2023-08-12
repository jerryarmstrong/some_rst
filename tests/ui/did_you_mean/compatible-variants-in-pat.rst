tests/ui/did_you_mean/compatible-variants-in-pat.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Foo {
    Bar(Bar),
}
struct Bar {
    x: i32,
}

fn a(f: Foo) {
    match f {
        Bar { x } => {
            //~^ ERROR mismatched types
            //~| HELP try wrapping
        }
    }
}

struct S;

fn b(s: Option<S>) {
    match s {
        S => {
            //~^ ERROR mismatched types
            //~| HELP try wrapping
            //~| HELP introduce a new binding instead
        }
        _ => {}
    }
}

fn c(s: Result<S, S>) {
    match s {
        S => {
            //~^ ERROR mismatched types
            //~| HELP try wrapping
            //~| HELP introduce a new binding instead
        }
        _ => {}
    }
}

fn main() {}


