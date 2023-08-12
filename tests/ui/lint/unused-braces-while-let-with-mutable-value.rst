tests/ui/lint/unused-braces-while-let-with-mutable-value.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![deny(unused_braces)]

fn main() {
    let mut a = Some(3);
    // Shouldn't warn below `a`.
    while let Some(ref mut v) = {a} {
        a.as_mut().map(|a| std::mem::swap(a, v));
        break;
    }
}


