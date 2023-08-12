tests/ui/hygiene/privacy.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(decl_macro)]

mod foo {
    fn f() {}

    pub macro m($e:expr) {
        f();
        self::f();
        ::foo::f();
        $e
    }
}

fn main() {
    foo::m!(
        foo::f() //~ ERROR `f` is private
    );
}


