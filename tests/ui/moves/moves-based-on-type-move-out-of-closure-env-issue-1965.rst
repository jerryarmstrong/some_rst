tests/ui/moves/moves-based-on-type-move-out-of-closure-env-issue-1965.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unboxed_closures, tuple_trait)]

fn to_fn<A:std::marker::Tuple,F:Fn<A>>(f: F) -> F { f }

fn test(_x: Box<usize>) {}

fn main() {
    let i = Box::new(3);
    let _f = to_fn(|| test(i)); //~ ERROR cannot move out
}


