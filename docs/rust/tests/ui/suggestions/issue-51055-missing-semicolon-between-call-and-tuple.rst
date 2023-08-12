tests/ui/suggestions/issue-51055-missing-semicolon-between-call-and-tuple.rs
============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn vindictive() -> bool { true }

fn perfidy() -> (i32, i32) {
    vindictive() //~ ERROR expected function, found `bool`
    (1, 2)
}

fn main() {}


