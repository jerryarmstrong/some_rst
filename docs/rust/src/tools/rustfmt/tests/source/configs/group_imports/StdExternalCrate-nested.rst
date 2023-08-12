src/tools/rustfmt/tests/source/configs/group_imports/StdExternalCrate-nested.rs
===============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-group_imports: StdExternalCrate
mod test {
    use crate::foo::bar;
    use std::path;
    use crate::foo::bar2;
}


