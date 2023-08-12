tests/ui/argument-suggestions/exotic-calls.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<T: Fn()>(t: T) {
    t(1i32);
    //~^ ERROR function takes 0 arguments but 1 argument was supplied
}

fn bar(t: impl Fn()) {
    t(1i32);
    //~^ ERROR function takes 0 arguments but 1 argument was supplied
}

fn baz() -> impl Fn() {
    || {}
}

fn baz2() {
    baz()(1i32)
    //~^ ERROR function takes 0 arguments but 1 argument was supplied
}

fn qux() {
    let x = || {};
    x(1i32);
    //~^ ERROR function takes 0 arguments but 1 argument was supplied
}

fn main() {}


