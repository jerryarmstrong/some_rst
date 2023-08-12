tests/ui/pattern/issue-88074-pat-range-type-inference-err.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Zero {
    const ZERO: Self;
}

impl Zero for String {
    const ZERO: Self = String::new();
}

fn foo() {
     match String::new() {
        Zero::ZERO ..= Zero::ZERO => {},
        //~^ ERROR only `char` and numeric types are allowed in range patterns
        _ => {},
    }
}

fn bar() {
    match Zero::ZERO {
        Zero::ZERO ..= Zero::ZERO => {},
        //~^ ERROR type annotations needed [E0282]
        _ => {},
    }
}

fn main() {
    foo();
    bar();
}


