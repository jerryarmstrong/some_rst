tests/ui/suggestions/option-content-move-from-tuple-match.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(a: &Option<String>, b: &Option<String>) {
    match (a, b) {
        //~^ ERROR cannot move out of a shared reference
        (None, &c) => &c.unwrap(),
        (&Some(ref c), _) => c,
    };
}

fn main() {}


