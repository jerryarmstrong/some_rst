tests/ui/consts/union_constant.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

union Uninit {
    _never_use: *const u8,
    uninit: (),
}

const UNINIT: Uninit = Uninit { uninit: () };
const UNINIT2: (Uninit,) = (Uninit { uninit: () }, );

fn main() {}


