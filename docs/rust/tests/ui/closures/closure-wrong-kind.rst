tests/ui/closures/closure-wrong-kind.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    /* Any copyright is dedicated to the Public Domain.
 * http://creativecommons.org/publicdomain/zero/1.0/ */

struct X;
fn foo<T>(_: T) {}
fn bar<T: Fn(u32)>(_: T) {}

fn main() {
    let x = X;
    let closure = |_| foo(x);  //~ ERROR E0525
    bar(closure);
}


