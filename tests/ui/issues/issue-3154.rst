tests/ui/issues/issue-3154.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Thing<'a, Q:'a> {
    x: &'a Q
}

fn thing<'a,Q>(x: &Q) -> Thing<'a,Q> {
    Thing { x: x } //~ ERROR explicit lifetime required in the type of `x` [E0621]
}

fn main() {
    thing(&());
}


