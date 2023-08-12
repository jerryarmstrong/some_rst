tests/ui/fmt/struct-field-as-captured-argument.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#[derive(Debug)]
struct Foo {
    field: usize,
}

fn main() {
    let foo = Foo { field: 0 };
    let bar = 3;
    format!("{foo.field}"); //~ ERROR invalid format string: field access isn't supported
    format!("{foo.field} {} {bar}", "aa"); //~ ERROR invalid format string: field access isn't supported
    format!("{foo.field} {} {1} {bar}", "aa", "bb"); //~ ERROR invalid format string: field access isn't supported
    format!("{foo.field} {} {baz}", "aa", baz = 3); //~ ERROR invalid format string: field access isn't supported
    format!("{foo.field:?} {} {baz}", "aa", baz = 3); //~ ERROR invalid format string: field access isn't supported
    format!("{foo.field:#?} {} {baz}", "aa", baz = 3); //~ ERROR invalid format string: field access isn't supported
    format!("{foo.field:.3} {} {baz}", "aa", baz = 3); //~ ERROR invalid format string: field access isn't supported
}


