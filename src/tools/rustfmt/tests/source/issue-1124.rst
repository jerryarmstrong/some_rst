src/tools/rustfmt/tests/source/issue-1124.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-reorder_imports: true

use d; use c; use b; use a; 
// The previous line has a space after the `use a;` 

mod a { use d; use c; use b; use a; }

use z;

use y;



use x;
use a;


