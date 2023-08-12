src/tools/rustfmt/tests/source/empty-item-single-line-false.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-brace_style: AlwaysNextLine
// rustfmt-empty_item_single_line: false

fn function()
{

}

struct Struct
{

}

enum Enum
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


