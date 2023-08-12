tests/ui/generator/drop-track-addassign-yield.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: -Zdrop-tracking

// Based on addassign-yield.rs, but with drop tracking enabled. Originally we did not implement
// the fake_read callback on ExprUseVisitor which caused this case to break.

#![feature(generators)]

fn foo() {
    let _y = static || {
        let x = &mut 0;
        *{
            yield;
            x
        } += match String::new() {
            _ => 0,
        };
    };

    // Please don't ever actually write something like this
    let _z = static || {
        let x = &mut 0;
        *{
            let inner = &mut 1;
            *{
                yield ();
                inner
            } += match String::new() {
                _ => 1,
            };
            yield;
            x
        } += match String::new() {
            _ => 2,
        };
    };
}

fn main() {
    foo()
}


