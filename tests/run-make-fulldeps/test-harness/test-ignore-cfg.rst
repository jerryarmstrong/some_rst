tests/run-make-fulldeps/test-harness/test-ignore-cfg.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[test]
#[cfg_attr(ignorecfg, ignore)]
fn shouldignore() {
}

#[test]
#[cfg_attr(noignorecfg, ignore)]
fn shouldnotignore() {
}


