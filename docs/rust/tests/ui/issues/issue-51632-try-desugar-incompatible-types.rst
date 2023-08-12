tests/ui/issues/issue-51632-try-desugar-incompatible-types.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]

fn missing_discourses() -> Result<isize, ()> {
    Ok(1)
}

fn forbidden_narratives() -> Result<isize, ()> {
    missing_discourses()?
    //~^ ERROR: `?` operator has incompatible types
}

fn main() {}


