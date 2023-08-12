tests/ui/did_you_mean/issue-38054-do-not-show-unresolved-names.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use Foo; //~ ERROR unresolved

use Foo1; //~ ERROR unresolved

fn main() {}


