tests/ui/lint/unused/unused-macro-with-bad-frag-spec.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused_macros)]

// Issue #21370

macro_rules! test {
    ($wrong:t_ty) => () //~ ERROR invalid fragment specifier `t_ty`
}

fn main() { }


