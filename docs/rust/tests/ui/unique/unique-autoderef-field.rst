tests/ui/unique/unique-autoderef-field.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

struct J { j: isize }

pub fn main() {
    let i: Box<_> = Box::new(J {
        j: 100
    });
    assert_eq!(i.j, 100);
}


