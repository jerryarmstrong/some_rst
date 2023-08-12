tests/ui/parser/recover-fn-trait-from-fn-kw.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(_: impl fn() -> i32) {}
//~^ ERROR expected identifier, found keyword `fn`

fn foo2<T: fn(i32)>(_: T) {}
//~^ ERROR expected identifier, found keyword `fn`

fn main() {
    foo(|| ());
    //~^ mismatched types
    foo2(|_: ()| {});
    //~^ type mismatch in closure arguments
}


