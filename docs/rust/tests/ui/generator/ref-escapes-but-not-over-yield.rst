tests/ui/generator/ref-escapes-but-not-over-yield.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generators)]

fn foo(x: &i32) {
    // In this case, a reference to `b` escapes the generator, but not
    // because of a yield. We see that there is no yield in the scope of
    // `b` and give the more generic error message.
    let mut a = &3;
    let mut b = move || {
        yield();
        let b = 5;
        a = &b;
        //~^ ERROR borrowed data escapes outside of generator
    };
}

fn main() { }


