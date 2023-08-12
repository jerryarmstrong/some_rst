tests/ui/imports/issue-8208.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use self::*; //~ ERROR: unresolved import `self::*` [E0432]
             //~^ cannot glob-import a module into itself

mod foo {
    use foo::*; //~ ERROR: unresolved import `foo::*` [E0432]
                //~^ cannot glob-import a module into itself

    mod bar {
        use super::bar::*;
        //~^ ERROR: unresolved import `super::bar::*` [E0432]
        //~| cannot glob-import a module into itself
    }

}

fn main() {
}


