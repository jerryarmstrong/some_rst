tests/ui/functions-closures/capture-clauses-boxed-closures.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn each<T, F>(x: &[T], mut f: F) where F: FnMut(&T) {
    for val in x {
        f(val)
    }
}

fn main() {
    let mut sum = 0_usize;
    let elems = [ 1_usize, 2, 3, 4, 5 ];
    each(&elems, |val| sum += *val);
    assert_eq!(sum, 15);
}


