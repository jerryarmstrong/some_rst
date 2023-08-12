src/tools/rustfmt/tests/target/issue-1124.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-reorder_imports: true

use a;
use b;
use c;
use d;
// The previous line has a space after the `use a;`

mod a {
    use a;
    use b;
    use c;
    use d;
}

use z;

use y;

use a;
use x;


