tests/ui/regions/regions-infer-borrow-scope-within-loop-ok.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn borrow<T>(x: &T) -> &T {x}

pub fn main() {
    let x: Box<_> = Box::new(3);
    loop {
        let y = borrow(&*x);
        assert_eq!(*x, *y);
        break;
    }
}


