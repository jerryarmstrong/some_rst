tests/ui/issues/auxiliary/issue-2316-b.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused_imports)]

extern crate issue_2316_a;

pub mod cloth {
    use issue_2316_a::*;

    pub enum fabric {
        gingham, flannel, calico
    }
}


