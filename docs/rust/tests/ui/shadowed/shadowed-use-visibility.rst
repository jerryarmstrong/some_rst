tests/ui/shadowed/shadowed-use-visibility.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod foo {
    pub fn f() {}

    use foo as bar;
    pub use self::f as bar;
}

mod bar {
    use foo::bar::f as g; //~ ERROR module import `bar` is private

    use foo as f;
    pub use foo::*;
}

use bar::f::f; //~ ERROR module import `f` is private
fn main() {}


