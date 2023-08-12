src/tools/rustfmt/tests/target/configs/reorder_imports/true.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-reorder_imports: true
// Reorder imports

use dolor;
use ipsum;
use lorem;
use sit;

fn foo() {
    use A;
    use B;
    use C;

    bar();

    use D;
    use E;
    use F;
}


