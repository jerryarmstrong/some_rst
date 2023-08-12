compiler/rustc_target/src/spec/i486_unknown_linux_gnu.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::Target;

pub fn target() -> Target {
    let mut base = super::i686_unknown_linux_gnu::target();
    base.cpu = "i486".into();
    base.llvm_target = "i486-unknown-linux-gnu".into();
    base
}


