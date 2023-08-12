tests/ui/generic-associated-types/issue-62326-parameter-out-of-range.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

trait Iterator {
    type Item<'a>: 'a;
}

impl Iterator for () {
    type Item<'a> = &'a ();
}

fn main() {}


