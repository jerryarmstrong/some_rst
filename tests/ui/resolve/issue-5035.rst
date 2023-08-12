tests/ui/resolve/issue-5035.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait I {}
type K = dyn I;
impl K for isize {} //~ ERROR expected trait, found type alias `K`

use ImportError; //~ ERROR unresolved import `ImportError` [E0432]
                 //~^ no `ImportError` in the root
impl ImportError for () {} // check that this is not an additional error (cf. issue #35142)

fn main() {}


