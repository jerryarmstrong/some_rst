tests/ui/issues/issue-3037.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616
#![allow(non_camel_case_types)]

enum what { }

fn what_to_string(x: what) -> String
{
    match x {
    }
}

pub fn main()
{
}


