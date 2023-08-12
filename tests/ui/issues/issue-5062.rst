tests/ui/issues/issue-5062.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() { format!("{:?}", None); }
    //~^ ERROR type annotations needed [E0282]


