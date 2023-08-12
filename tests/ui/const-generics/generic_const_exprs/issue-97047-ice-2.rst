tests/ui/const-generics/generic_const_exprs/issue-97047-ice-2.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(adt_const_params, generic_const_exprs)]
//~^ WARN the feature `adt_const_params` is incomplete and may not be safe to use and/or cause compiler crashes [incomplete_features]
//~^^ WARN the feature `generic_const_exprs` is incomplete and may not be safe to use and/or cause compiler crashes [incomplete_features]

pub struct Changes<const CHANGES: &'static [&'static str]>
where
    [(); CHANGES.len()]:,
{
    changes: [usize; CHANGES.len()],
}

impl<const CHANGES: &'static [&'static str]> Changes<CHANGES>
where
    [(); CHANGES.len()]:,
{
    pub fn combine(&mut self, other: &Self) {
        for _change in &self.changes {}
    }
}

pub fn main() {}


