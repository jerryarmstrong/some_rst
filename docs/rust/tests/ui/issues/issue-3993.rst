tests/ui/issues/issue-3993.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use zoo::fly; //~ ERROR: function `fly` is private

mod zoo {
    fn fly() {}
}


fn main() {
    fly();
}


