src/tools/rustfmt/tests/source/configs/reorder_imports/true.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-reorder_imports: true
// Reorder imports

use lorem;
use ipsum;
use dolor;
use sit;

fn foo() {
    use C;
    use B;
    use A;

    bar();

    use F;
    use E;
    use D;
}


