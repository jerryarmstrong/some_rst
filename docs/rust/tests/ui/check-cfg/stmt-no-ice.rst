tests/ui/check-cfg/stmt-no-ice.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This test checks that there is no ICE with this code
//
// check-pass
// compile-flags:--check-cfg=names() -Z unstable-options

fn main() {
    #[cfg(crossbeam_loom)]
    //~^ WARNING unexpected `cfg` condition name
    {}
}


