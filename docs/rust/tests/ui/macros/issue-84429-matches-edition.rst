tests/ui/macros/issue-84429-matches-edition.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021
// check-pass
//
// Regression test for issue #84429
// Tests that we can properly invoke `matches!` from a 2021-edition crate.

fn main() {
    let _b = matches!(b'3', b'0' ..= b'9');
}


