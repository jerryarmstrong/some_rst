tests/ui/pattern/usefulness/refutable-pattern-in-fn-arg.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let f = |3: isize| println!("hello");
    //~^ ERROR refutable pattern in function argument
    //~| `_` not covered
    f(4);
}


