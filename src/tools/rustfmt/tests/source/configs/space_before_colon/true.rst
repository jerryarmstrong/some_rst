src/tools/rustfmt/tests/source/configs/space_before_colon/true.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-space_before_colon: true
// Space before colon

fn lorem<T : Eq>(t : T) {
    let ipsum: Dolor = sit;
}

const LOREM : Lorem = Lorem {
    ipsum : dolor,
    sit : amet,
};


