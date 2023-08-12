tests/ui/binding/borrowed-ptr-pattern-option.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn select<'r>(x: &'r Option<isize>, y: &'r Option<isize>) -> &'r Option<isize> {
    match (x, y) {
        (&None, &None) => x,
        (&Some(_), _) => x,
        (&None, &Some(_)) => y
    }
}

pub fn main() {
    let x = None;
    let y = Some(3);
    assert_eq!(select(&x, &y).unwrap(), 3);
}


