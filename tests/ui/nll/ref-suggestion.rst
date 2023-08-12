tests/ui/nll/ref-suggestion.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x = vec![1];
    let y = x;
    x; //~ ERROR use of moved value

    let x = vec![1];
    let mut y = x;
    x; //~ ERROR use of moved value

    let x = (Some(vec![1]), ());

    match x {
        (Some(y), ()) => {},
        _ => {},
    }
    x; //~ ERROR use of partially moved value
}


