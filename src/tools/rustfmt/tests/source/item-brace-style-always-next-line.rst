src/tools/rustfmt/tests/source/item-brace-style-always-next-line.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-brace_style: AlwaysNextLine

mod M {
    enum A {
        A,
    }

    struct B {
        b: i32,
    }

    // For empty enums and structs, the brace remains on the same line.
    enum C {}

    struct D {}

    enum A<T> where T: Copy {
        A,
    }

    struct B<T> where T: Copy {
        b: i32,
    }

    // For empty enums and structs, the brace remains on the same line.
    enum C<T> where T: Copy {}

    struct D<T> where T: Copy {}
}


fn function()
{

}

trait Trait
{

}

impl<T> Trait for T
{

}

trait Trait2<T>
where
    T: Copy + Display + Write + Read + FromStr, {}

trait Trait3<T>
where
    T: Something
        + SomethingElse
        + Sync
        + Send
        + Display
        + Debug
        + Copy
        + Hash
        + Debug
        + Display
        + Write
        + Read, {}


