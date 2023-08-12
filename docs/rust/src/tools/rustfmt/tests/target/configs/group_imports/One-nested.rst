src/tools/rustfmt/tests/target/configs/group_imports/One-nested.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-group_imports: One
mod test {
    use crate::foo::bar;
    use crate::foo::bar2;
    use std::path;
}


