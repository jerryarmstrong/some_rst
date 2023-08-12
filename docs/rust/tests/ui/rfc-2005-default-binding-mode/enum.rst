tests/ui/rfc-2005-default-binding-mode/enum.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Wrapper {
    Wrap(i32),
}

use Wrapper::Wrap;

pub fn main() {
    let Wrap(x) = &Wrap(3);
    *x += 1; //~ ERROR cannot assign to `*x`, which is behind a `&` reference


    if let Some(x) = &Some(3) {
        *x += 1; //~ ERROR cannot assign to `*x`, which is behind a `&` reference
    } else {
        panic!();
    }

    while let Some(x) = &Some(3) {
        *x += 1; //~ ERROR cannot assign to `*x`, which is behind a `&` reference
        break;
    }
}


