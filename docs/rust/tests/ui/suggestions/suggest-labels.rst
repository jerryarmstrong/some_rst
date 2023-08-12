tests/ui/suggestions/suggest-labels.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[allow(unreachable_code, unused_labels)]
fn main() {
    'foo: loop {
        break 'fo; //~ ERROR use of undeclared label
    }

    'bar: loop {
        continue 'bor; //~ ERROR use of undeclared label
    }

    'longlabel: loop {
        'longlabel1: loop {
            break 'longlable; //~ ERROR use of undeclared label
        }
    }
}


