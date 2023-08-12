tests/ui/unboxed-closures/unboxed-closures-move-from-projection-issue-30046.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused)]

fn foo<F>(f: F)
    where F: FnOnce()
{
}

fn main() {
    // Test that this closure is inferred to `FnOnce`
    // because it moves from `y.as<Option::Some>.0`:
    let x = Some(vec![1, 2, 3]);
    foo(|| {
        match x {
            Some(y) => { }
            None => { }
        }
    });

    // Test that this closure is inferred to `FnOnce`
    // because it moves from `y.0`:
    let y = (vec![1, 2, 3], 0);
    foo(|| {
        let x = y.0;
    });
}


